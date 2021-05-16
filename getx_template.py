'''
Este script fue creado con el fin de automatizar la tediosa tarea de
crear la estructura de carpetas necesarias para trabajar con Getx en Flutter,
ademas de crear la estructura de carpeta tambien crea una pantalla todas
las demas clases necesarias.

Autor: Joinner Medina.
'''

import os

def main():
    
    # Contiene la carpeta base donde se crearan
    # las demas carpetas
    baseFolder = '.\\lib\\app'
    
    # Lista de carpetas dentro de app
    appFolder = [
        'bindings',
        'controllers',
        'data',
        'routes',
        'translations',
        'ui',
    ]
    
    # Lista de carpetas dentro de data
    dataFolder = [
        'model',
        'provider',
        'repository'
    ]
    
    # Lista de carpetas dentro de ui
    uiFolder = [
        'pages',
        'global_widgets',
        'theme',
        'utils',
    ]
    
    BINDINGS = '''
import 'package:get/get.dart';
import '../controllers/home_controller.dart';

class HomeBinding implements Bindings {
  @override
  void dependencies() {
    Get.lazyPut<HomeController>(() => HomeController());
  }
}
    '''
    CONTROLLER = '''
import 'package:get/get.dart';

class HomeController extends GetxController {
}
    '''
    
    HOMEPAGE = '''
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../../../controllers/home_controller.dart';

class HomePage extends GetView<HomeController> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('HomePage'),
      ),
      body: SafeArea(
        child: Text('HomeController'),
      ),
    );
  }
}
    '''
    
    APPPAGES = '''
import 'package:get/get.dart';
import '../ui/pages/home_page/home_page.dart';
part 'app_routes.dart';

class AppPages {
  static final routes = [
    GetPage(name: Routes.INITIAL, page: () => HomePage()),
  ];
}
    '''
    
    APPROUTES = '''
part of './app_pages.dart';

abstract class Routes {
  static const INITIAL = 'homePage';
}
    '''
    
    MAIN = '''
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'app/bindings/home_bindigs.dart';
import 'app/routes/app_pages.dart';

void main() {
  runApp(
    GetMaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: Routes.INITIAL,
      defaultTransition: Transition.fade,
      initialBinding: HomeBinding(),
      getPages: AppPages.routes,
    ),
  );
}
    '''
    
    # Funcion que construye la estructura de carpetas
    def foldersGenerator():
        for folders in appFolder:
                os.mkdir(baseFolder + '\\' + folders)
                
        if os.path.exists(baseFolder + '\\data'):
            for folders in dataFolder:
                os.mkdir(baseFolder + '\\data' + '\\' + folders)
                        
        if os.path.exists(baseFolder + '\\ui'):
            for folders in uiFolder:
                os.mkdir(baseFolder + '\\ui' + '\\' + folders)

        if os.path.exists(baseFolder + '\\ui\\pages'):
            os.mkdir(baseFolder + '\\ui\\pages\\home_page')
    
    # Funcion que genera las clases necesarias y escribe el codigo
    # que necesita cada clase. 
    def classGenerator(textWrite, className, folderValidation, routeFile):
        if os.path.exists(baseFolder + folderValidation):
            className = className + '.dart'
            file = open(baseFolder + routeFile + '\\' + className, 'x')
            file.write(textWrite)
        return file
    
    # Elimina el contenido del metodo main para poder
    # escribir el codigo necesario.
    def mainModification():
        if (os.path.exists('.\\lib')):
            file = open('.\\lib' + '\\' + 'main.dart', 'r+')
            file.truncate(0)
            file.write(MAIN)
            file.close
        
    try:
        if not os.path.exists(baseFolder):
            os.mkdir('.\\lib\\app')
            
        if os.path.exists(baseFolder):
            # Se crean las carpetas 
            foldersGenerator()
            
            # Crea la clase binding
            classGenerator(
                textWrite=BINDINGS,
                className='home_bindigs',
                folderValidation='\\bindings',
                routeFile='\\bindings'
            )
            
            # Crea la clase controller
            classGenerator(
                textWrite=CONTROLLER,
                className='home_controller',
                folderValidation='\\controllers',
                routeFile='\\controllers'
            )
            
            # Crea la clase HomePage
            classGenerator(
                textWrite=HOMEPAGE,
                className='home_page',
                folderValidation='\\ui\\pages\\home_page',
                routeFile='\\ui\\pages\\home_page'
            )
            
            # Crea la clase AppPages
            classGenerator(
                textWrite=APPPAGES,
                className='app_pages',
                folderValidation='\\routes',
                routeFile='\\routes'
            )
            
            # Crea la clase AppRoutes
            classGenerator(
                textWrite=APPROUTES,
                className='app_routes',
                folderValidation='\\routes',
                routeFile='\\routes'
            )
            
            # Modifica el metodo main
            mainModification()
         
    except OSError as error:
        print(error)
    
    
if __name__=="__main__":
    main()