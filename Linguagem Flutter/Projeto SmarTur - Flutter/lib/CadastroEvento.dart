import 'package:flutter/material.dart';
import 'helper/anotacaoHelper.dart';
import 'model/Evento.dart';
import 'package:intl/intl.dart';
import 'package:intl/date_symbol_data_local.dart';

class CadastroEvento extends StatefulWidget {
  @override
  _HomesState createState() => _HomesState();
}

class _HomesState extends State<CadastroEvento> {

  TextEditingController _tituloController = TextEditingController();
  TextEditingController _descricaoController = TextEditingController();
  TextEditingController _dataeventoController = TextEditingController();
  TextEditingController _precoController = TextEditingController();



  var _db = AnotacaoHelper();
  List<Evento> _eventos = List<Evento>();


  _exibirTelaCadastro( {Evento evento} ){

    String textoSalvarAtualizar = "";
    if (evento == null){//criando evento
      _tituloController.text="";
      _descricaoController.text="";
      _precoController.text = "";
      _dataeventoController.text = "";
      textoSalvarAtualizar = "Criar";
    }else{//atualizando evento
      _tituloController.text = evento.titulo;
      _descricaoController.text = evento.descricao;
      _precoController.text = evento.preco;
      _dataeventoController.text = evento.data_evento;
      textoSalvarAtualizar = "Atualizar";
    }

    showDialog(
        context: context,
        builder: (context){
          return AlertDialog(
            title: Text("$textoSalvarAtualizar evento"),
            contentPadding: new EdgeInsets.symmetric(vertical: 2.0, horizontal: 5.5),
            content: Column(
              //mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                TextField(
                  controller: _tituloController,
                  autofocus: true,
                  decoration: InputDecoration(
                      labelText: "Título",
                      hintText: "Digite título...",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.0, horizontal: 1.5),
                  ),
                ),
                TextField(
                  controller: _descricaoController,
                  decoration: InputDecoration(
                      labelText: "Descrição",
                      hintText: "Digite descrição...",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.5, horizontal: 1.5),
                  ),
                ),
                TextField(
                  controller: _dataeventoController,
                  decoration: InputDecoration(
                      labelText: "Data do Evento",
                      hintText: "Ex: 20/12/2020",
                      contentPadding: new EdgeInsets.symmetric(vertical: 0.5, horizontal: 1.5),
                  ),
                ),
                TextField(
                  controller: _precoController,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                    labelText: "Preço",
                    hintText: "Ex: 40R\$",
                    contentPadding: new EdgeInsets.symmetric(vertical: 0.5, horizontal: 1.5),
                  ),
                ),
              ],
            ),
            actions: <Widget> [
              FlatButton(
                onPressed: () => Navigator.pop(context),
                child: Text("Cancelar"),
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
    String preco = _precoController.text;
    String data_evento = _dataeventoController.text;


    if (eventoSelecionada == null){//salvando evento
      Evento evento = Evento(titulo,descricao,DateTime.now().toString(),"Presença não Confirmada",data_evento,preco);
      int resultado = await _db.salvarEvento(evento);
    }else{//atualizando evento
      eventoSelecionada.titulo = titulo;
      eventoSelecionada.descricao = descricao;
      eventoSelecionada.data = DateTime.now().toString();
      eventoSelecionada.data_evento = data_evento;
      eventoSelecionada.preco = preco;

      int resultado = await _db.atualizarEvento(eventoSelecionada);

    }


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

  _removerEvento(int id) async{
    await _db.removerEvento(id);
    _recuperarEvento();
  }

  @override
  void initState() {
    super.initState();
    _recuperarEvento();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Lista de Eventos"),
        centerTitle: true,
        backgroundColor: Colors.blue,
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
                    title: Text("${evento.titulo} - Data: ${evento.data_evento}"),
                    subtitle: Text("${evento.descricao} - Preço: ${evento.preco}R\$"),
                    trailing: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: <Widget>[
                        GestureDetector(
                          onTap: (){
                            _exibirTelaCadastro(evento: evento);
                          },
                          child: Padding(
                            padding: EdgeInsets.only(right: 16),
                            child: Icon(
                              Icons.edit,
                              color: Colors.blue,
                            ),
                          ),
                        ),
                        GestureDetector(
                          onTap: (){
                            _removerEvento(evento.id);
                          },
                          child: Padding(
                            padding: EdgeInsets.only(right: 0),
                            child: Icon(
                              Icons.remove_circle,
                              color: Colors.red,
                            ),
                          ),
                        )
                      ],
                    ),
                  ),
                );
              },
            ),
          )
        ],
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.green,
        foregroundColor: Colors.white,
        child: Icon(Icons.add),
        onPressed: (){
          _exibirTelaCadastro();
        },
      ),
    );
  }
}
