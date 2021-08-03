
class Evento {

  int id;
  String titulo;
  String descricao;
  String data;
  String data_evento;
  String preco;
  String confirma_evento;


  Evento(this.titulo,this.descricao,this.data,this.confirma_evento,this.data_evento,this.preco);


  Evento.fromMap(Map map){
    this.id = map["id"];
    this.titulo = map["titulo"];
    this.descricao = map["descricao"];
    this.data = map["data"];
    this.data_evento = map["data_evento"];
    this.preco = map["preco"];
    this.confirma_evento = map["confirma_evento"];

  }

  Map toMap(){
    Map<String, dynamic> map = {
      "titulo": this.titulo,
      "descricao": this.descricao,
      "data": this.data,
      "data_evento": this.data_evento,
      "preco": this.preco,
      "confirma_evento": this.confirma_evento,
    };

    if (this.id != null) {
      map["id"] = this.id;
    }
    return map;
  }

}