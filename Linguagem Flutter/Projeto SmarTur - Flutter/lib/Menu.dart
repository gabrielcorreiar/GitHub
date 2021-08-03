import 'package:flutter/material.dart';
import 'helper/anotacaoHelper.dart';
import 'model/Evento.dart';
import 'package:intl/intl.dart';
import 'package:intl/date_symbol_data_local.dart';

class MyMenu extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Drawer',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      //home: MyHomePage(title: 'Drawer'), // versão antiga
      home: Home(title: 'Drawer'),
    );
  }
}

class Home extends StatefulWidget {
  @override

  final String title;
  const Home({Key key, this.title}) : super(key: key);

  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  int currItem = 0;

  TextEditingController _tituloController = TextEditingController();
  TextEditingController _descricaoController = TextEditingController();
  TextEditingController _confirmacaoeventoController = TextEditingController();
  TextEditingController _dataeventoController = TextEditingController();
  TextEditingController _precoController = TextEditingController();

  var _db = AnotacaoHelper();
  List<Evento> _eventos = List<Evento>();


  _exibirConfirmacao( {Evento evento} ){

    String textoSalvarAtualizar = "Confirmar";
    if (evento != null){


      _tituloController.text = evento.titulo;
      _descricaoController.text = evento.descricao;
      _confirmacaoeventoController.text = evento.confirma_evento;
       _dataeventoController.text = evento.data_evento;
       _precoController.text = evento.preco;

      if (evento.confirma_evento == "Presença Confirmada") {
        textoSalvarAtualizar = "";
      }

    }


    showDialog(
        context: context,
        builder: (context){
          return AlertDialog(
            title: Text("Evento"),
           contentTextStyle: TextStyle(fontStyle: FontStyle.normal),
            contentPadding: new EdgeInsets.symmetric(vertical: 10.0, horizontal: 10.5),
            content: Column(
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                TextField(
                  enabled: false,
                  controller: _tituloController,
                  autofocus: true,
                  decoration: InputDecoration(
                      labelText: "Título",
                      hintText: "Digite título...",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.0, horizontal: 1.5),
                  ),
                ),
                TextField(
                  enabled: false,
                  controller: _descricaoController,
                  decoration: InputDecoration(
                      labelText: "Descrição",
                      hintText: "Digite descrição...",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.0, horizontal: 1.5),
                  ),
                ),
                TextField(
                  enabled: false,
                  controller: _dataeventoController,
                  decoration: InputDecoration(
                    labelText: "Data do Evento",
                    hintText: "Digite descrição...",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.0, horizontal: 1.5),
                  ),
                ),
                TextField(
                  enabled: false,
                  controller: _precoController,
                  decoration: InputDecoration(
                    labelText: "Preço",
                    hintText: "Digite descrição...",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.0, horizontal: 1.5),
                  ),
                ),
                TextField(
                  enabled: false,
                  controller: _confirmacaoeventoController,
                  decoration: InputDecoration(
                    labelText: "Status",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.0, horizontal: 1.5),
                  ),
                ),
              ],
            ),
            actions: <Widget> [
              FlatButton(
                onPressed: () => Navigator.pop(context),
                child: Text("Voltar"),
              ),
              FlatButton(
                onPressed: (){
                  _salvarAtualizarEvento(eventoSelecionada: evento);
                  Navigator.pop(context);
                },
                child: Text(textoSalvarAtualizar),

              )
            ],

          );
        }
    );
  }


  _recuperarEvento() async{

    List eventosRecuperados = await _db.recuperarEvento();

    List<Evento> listaTemporaria = List<Evento>();
    for (var item in eventosRecuperados) {

      Evento evento = Evento.fromMap(item);
      listaTemporaria.add(evento);

    }

    setState(() {
      _eventos = listaTemporaria;
    });

    listaTemporaria = null;


  }

  _salvarAtualizarEvento({Evento eventoSelecionada}) async {
    String titulo = _tituloController.text;
    String descricao = _descricaoController.text;
    String confirmacao =_confirmacaoeventoController.text;

    if (eventoSelecionada != null){
      eventoSelecionada.titulo = titulo;
      eventoSelecionada.descricao = descricao;
      eventoSelecionada.data = DateTime.now().toString();
      eventoSelecionada.confirma_evento = "Presença Confirmada";
    }

    int resultado = await _db.atualizarEvento(eventoSelecionada);




    _tituloController.clear();
    _descricaoController.clear();
    _recuperarEvento();

  }

  _formatarData(String data){

    initializeDateFormatting("pt_BR");

    var formatador = DateFormat("dd/MM/y H:m");

    DateTime dataConvertida = DateTime.parse(data);
    String dataFormatada = formatador.format(dataConvertida);

    return dataFormatada;

  }

  @override
  void initState() {
    super.initState();
    _recuperarEvento();
  }


  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(title: Text("Smartur - Eventos",
      ),
        centerTitle: true,
      ),
      body: Column(
        children: <Widget>[
          Expanded(
            child: ListView.builder(
              itemCount: _eventos.length,
              itemBuilder: (context, index){
                final evento = _eventos[index];
                return Card(
                  child: ListTile(
                    //  title: Text(evento.titulo),
                    title: Text("${evento.titulo} - ${evento.confirma_evento}"),
                    subtitle: Text("Data: ${evento.data_evento} Preço: ${evento.preco}R\$"),
                    trailing: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: <Widget>[
                        GestureDetector(

                          onTap: (){
                            _exibirConfirmacao(evento: evento);
                          },
                          child: Padding(
                            padding: EdgeInsets.only(right: 16),
                            // child: _color(),
                            child:Icon(
                              Icons.check,
                              color: Colors.green,
                            ),

                          ),
                        ),

                      ],
                    ),
                  ),
                );
              },
            ),
          )

        ],
      ),

      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            UserAccountsDrawerHeader(
              accountEmail: Text("user@mail.com"),
              accountName: Text("User"),
              currentAccountPicture: CircleAvatar(
                child: Text("User"),
              ),

            ),
            ListTile(
              leading: Icon(Icons.person),
              title: Text("Minha conta"),
              onTap: () {
                Navigator.pop(context);
                //Navegar para outra página
              },
            ),
            ListTile(
              leading: Icon(Icons.favorite),
              title: Text("Favoritos"),
              onTap: () {
                Navigator.pop(context);
                //Navegar para outra página
              },
            ),
          ],
        ),
      ),
    );
  }

}