import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:geolocator/geolocator.dart';
import 'dart:async';
import 'package:cloud_firestore/cloud_firestore.dart';

class Geolocalizacao extends StatefulWidget {

  String idViagem;

  Geolocalizacao({ this.idViagem });

  @override
  _GeolocalizacaoState createState() => _GeolocalizacaoState();
}

class _GeolocalizacaoState extends State<Geolocalizacao> {

  Completer<GoogleMapController> _controller = Completer();
  Set<Marker> _marcadores = {};
  CameraPosition _posicaoCamera = CameraPosition(
      target: LatLng(-23.562436, -46.655005),
      zoom: 1000
  );
  Firestore _db = Firestore.instance;

  _onMapCreated( GoogleMapController controller ){
    _controller.complete( controller );
  }

  _adicionarMarcador( LatLng latLng ) async {

    List<Placemark> listaEnderecos = await Geolocator()
        .placemarkFromCoordinates(latLng.latitude, latLng.longitude);

    if( listaEnderecos != null && listaEnderecos.length > 0 ){

      Placemark endereco = listaEnderecos[0];
      String rua = endereco.thoroughfare;

      //41.890250, 12.492242
      Marker marcador = Marker(
          markerId: MarkerId("marcador-${latLng.latitude}-${latLng.longitude}"),
          position: latLng,
          infoWindow: InfoWindow(
              title: rua
          )
      );

      setState(() {
        _marcadores.add( marcador );

        //Salva no firebase
        Map<String, dynamic> viagem = Map();
        viagem["titulo"] = rua;
        viagem["latitude"] = latLng.latitude;
        viagem["longitude"] = latLng.longitude;

        _db.collection("viagens")
            .add( viagem );

      });

    }

  }

  _movimentarCamera() async {

    GoogleMapController googleMapController = await _controller.future;
    googleMapController.animateCamera(
        CameraUpdate.newCameraPosition(
            _posicaoCamera
        )
    );

  }

  _adicionarListenerLocalizacao(){

    //-23.579934, -46.660715

    var geolocator = Geolocator();
    var locationOptions = LocationOptions(accuracy: LocationAccuracy.high);
    geolocator.getPositionStream( locationOptions ).listen((Position position){

      setState(() {
        _posicaoCamera = CameraPosition(
            target: LatLng(position.latitude, position.longitude),
            zoom: 18
        );
        _movimentarCamera();
      });

    });

  }

  _recuperaViagemParaID(String idViagem) async {

    if( idViagem != null ){

      //exibir marcador para id viagem
      DocumentSnapshot documentSnapshot = await _db
          .collection("viagens")
          .document( idViagem )
          .get();

      var dados = documentSnapshot.data;

      String titulo = dados["titulo"];
      LatLng latLng = LatLng(
          dados["latitude"],
          dados["longitude"]
      );

      setState(() {

        Marker marcador = Marker(
            markerId: MarkerId("marcador-${latLng.latitude}-${latLng.longitude}"),
            position: latLng,
            infoWindow: InfoWindow(
                title: titulo
            )
        );

        _marcadores.add( marcador );
        _posicaoCamera = CameraPosition(
            target: latLng,
            zoom: 18
        );
        _movimentarCamera();

      });

    }else{
      _adicionarListenerLocalizacao();
    }

  }

  @override
  void initState() {
    super.initState();

    //Recupera viagem pelo ID
    _recuperaViagemParaID( widget.idViagem );

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Mapa"),backgroundColor: Colors.blue,),
      body: Container(
        child: GoogleMap(
          markers: _marcadores,
          mapType: MapType.normal,
          initialCameraPosition: _posicaoCamera,
          onMapCreated: _onMapCreated,
          onLongPress: _adicionarMarcador,
        ),
      ),
    );
  }
}

