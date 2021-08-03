/*import 'package:smarturv1/model/Evento.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class AnotacaoHelper {

  static final String nomeTabela = "eventos";
  static final AnotacaoHelper _anotacaoHelper = AnotacaoHelper._internal();
  Database _db;

  factory AnotacaoHelper(){
    return _anotacaoHelper;
  }

  AnotacaoHelper._internal(){
  }

  get db async{
    if(_db != null){
      return _db;
    }else{
      _db = await inicializarDB();
      return _db;
    }
  }

  _onCreate(Database db, int version) async {
    String sql = "CREATE TABLE $nomeTabela ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "titulo VARCHAR, "
        "descricao TEXT, "
        "data DATETIME)";
  await db.execute(sql);
  }


  inicializarDB() async {
    final caminhoBancoDados = await getDatabasesPath();
    final localBancoDados = join(caminhoBancoDados,"Banco_Smartur.db");
    
    var db = await openDatabase(localBancoDados,version: 1,onCreate: _onCreate);

    return db;
  }

  Future<int> salvarEvento(Evento evento) async {

    var bancoDados = await db;

    int resultado = await bancoDados.insert(nomeTabela, evento.toMap() );
    return resultado;
  }

  recuperarEvento() async {

    var bancoDados = await db;
    String sql = "Select * from $nomeTabela Order BY data DESC";
    List eventos = await bancoDados.rawQuery( sql );
    return eventos;

  }

  Future<int> atualizarEvento(Evento evento) async {

    var bancoDados = await db;

    return await bancoDados.update(nomeTabela, evento.toMap(),where: "id=?",whereArgs:[evento.id] );

  }

  Future<int> removerEvento(int id) async {

    var bancoDados = await db;
    return await bancoDados.delete(nomeTabela, where: "id=?",whereArgs:[id] );

  }

}*/

import 'package:smarturv1/model/Evento.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class AnotacaoHelper {

  //static final String nomeTabela = "vv";
  static final String nomeTabela = "eventos"; //Mudar nome de tabela para Testar
  static final AnotacaoHelper _anotacaoHelper = AnotacaoHelper._internal();
  Database _db;

  factory AnotacaoHelper(){
    return _anotacaoHelper;
  }

  AnotacaoHelper._internal(){
  }

  get db async{
    if(_db != null){
      return _db;
    }else{
      _db = await inicializarDB();
      return _db;
    }
  }

  _onCreate(Database db, int version) async {
    String sql = "CREATE TABLE IF NOT EXISTS $nomeTabela ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "titulo VARCHAR, "
        "descricao TEXT, "
        "data DATETIME, "
        "confirma_evento VARCHAR,"
        "data_evento VARCHAR,"
        "preco VARCHAR)";


  await db.execute(sql);
  }


  inicializarDB() async {
    final caminhoBancoDados = await getDatabasesPath();
    final localBancoDados = join(caminhoBancoDados,"Banco_Smartur.db");
    //final localBancoDados = join(caminhoBancoDados,"teste.db");

    var db = await openDatabase(localBancoDados,version: 1,onCreate: _onCreate);

    return db;
  }

  Future<int> salvarEvento(Evento evento) async {

    var bancoDados = await db;

    int resultado = await bancoDados.insert(nomeTabela, evento.toMap() );
    return resultado;
  }

  recuperarEvento() async {

    inicializarDB();

    var bancoDados = await db;


    String sql = "Select * from $nomeTabela Order BY data DESC";

    String create = "CREATE TABLE IF NOT EXISTS $nomeTabela ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "titulo VARCHAR, "
        "descricao TEXT, "
        "data DATETIME, "
        "confirma_evento VARCHAR,"
        "data_evento VARCHAR,"
        "preco VARCHAR)";


    await bancoDados.rawQuery( create );
    List eventos = await bancoDados.rawQuery( sql );


    return eventos;

  }

  Future<int> atualizarEvento(Evento evento) async {

    var bancoDados = await db;

    return await bancoDados.update(nomeTabela, evento.toMap(),where: "id=?",whereArgs:[evento.id] );

  }

  Future<int> removerEvento(int id) async {

    var bancoDados = await db;
    return await bancoDados.delete(nomeTabela, where: "id=?",whereArgs:[id] );

  }

}