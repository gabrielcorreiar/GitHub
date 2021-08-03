import 'package:flutter/material.dart';
import 'package:smarturv1/CadastroEvento.dart';
import 'package:smarturv1/Geolocalizacao.dart';
import 'package:smarturv1/Menu.dart';


class MyAppNavigation extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Drawer',
      theme: ThemeData(
        primarySwatch: Colors.pink,
      ),
      home: MyHomePage(title: 'Drawer'), // versão antiga
      //home: Home(title: 'Drawer'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;

  const MyHomePage({Key key, this.title}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}


class _MyHomePageState extends State<MyHomePage> {

  int _selectedIndex = 0;

  static int currItem = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _getBody(currItem),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: currItem,
        onTap: (value) => setState(() => currItem = value),
        items: [
          BottomNavigationBarItem(
            icon: Icon(
              Icons.home,
            ),
            title: Text(
              "Explore",
            ),
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.add_circle,
            ),
            title: Text(
              "Create",
            ),
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.search,
            ),
            title: Text(
              "Search",
            ),
          ),

        ],
        type: BottomNavigationBarType.fixed,
      ),
    );
  }

  Widget _getBody(int currItem) {
    switch (currItem) {
      case 0:
        return MyMenu(); //Página de Menu
      case 1:
        return CadastroEvento();// Página de Cadastro de Evento
      case 2:
      return Geolocalizacao();

    }

    return Center(child: Text(""),);
  }
}
