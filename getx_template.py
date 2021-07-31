'''
Este script fue creado con el fin de automatizar la tediosa tarea de
crear la estructura de carpetas necesarias para trabajar con Getx en Flutter,
ademas de crear la estructura de carpeta tambien crea una pantalla todas
las demas clases necesarias.

Autor: Joinner Medina.
'''

import os


def main_code():

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

    def linter_for_dart(textWrite):
        if os.path.exists('.\\analysis_options.yaml'):
            print('El archivo analysis_options.yaml, ya existe')
        else:
            file = open('.\\analysis_options.yaml', 'x')
            file.write(textWrite)

    # Elimina el contenido del metodo main para poder
    # escribir el codigo necesario.
    def mainModification():
        if (os.path.exists('.\\lib')):
            file = open('.\\lib' + '\\' + 'main.dart', 'r+')
            file.truncate(0)
            file.write(MAIN)
            file.close

    def bindings_code():
        return '''
    import 'package:get/get.dart';
    import '../controllers/home_controller.dart';

    class HomeBinding implements Bindings {
      @override
      void dependencies() {
        Get.lazyPut<HomeController>(() => HomeController());
      }
    }
        '''

    def controller_code():
        return '''
    import 'package:get/get.dart';

    class HomeController extends GetxController {
    }
        '''

    def home_page_code():
        return '''
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

    def app_pages_code():
        return '''
    import 'package:get/get.dart';
    import '../ui/pages/home_page/home_page.dart';
    part 'app_routes.dart';

    class AppPages {
      static final routes = [
        GetPage(name: Routes.INITIAL, page: () => HomePage()),
      ];
    }
        '''

    def app_routes_code():
        return '''
    part of './app_pages.dart';

    abstract class Routes {
      static const INITIAL = 'homePage';
    }
        '''

    def main_code():
        return '''
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

    def linter_code():
        return '''
    #lintes personalizable, puede agregar o eliminar reglas, según sus necesidades.
    #Para hacerlo, debe crear un archivo analysis_options.yaml a la altura de su carpeta raiz. 

    linter:
      rules:
        # ---------------------------------------------------------------------------- #
        #                                     STYLE                                    #
        # ---------------------------------------------------------------------------- #
        # ------ Disable individual rules ----- #
        #                 ---                   #
        # Turn off what you don't like.         #
        # ------------------------------------- #

        # Use parameter order as in json response
        always_put_required_named_parameters_first: false
        
        # Util classes are awesome!
        avoid_classes_with_only_static_members: false
        
        # Prefiere const con constructores constantes
        prefer_const_constructors: true

        # Organiza el codigo en formato cascada para evitar
        # redundancia
        cascade_invocations: true

        # Good packages document everything
        public_member_api_docs: true
        
        # Blindly follow the Flutter code style, which prefers types everywhere
        always_specify_types: true
      
        # Back to the 80s
        lines_longer_than_80_chars: false

        # Evite las funciones asíncronas que devuelven vacío.
        avoid_void_async: true

        # ---------------------------------------------------------------------------- #
        #                                 ERRORS RULES                                 #
        # ---------------------------------------------------------------------------- #
        
        # Evite las llamadas al print en el código de producción.
        avoid_print: true
        
        # Evite las importaciones relativas de archivos en formato lib/.
        avoid_relative_lib_imports: true

        # Evita devolver Futures nulos.
        avoid_returning_null_for_future: true

        # Evitar .toString () en el código de producción ya que los resultados pueden minimizarse.
        avoid_type_to_string: true

        # Evite tipos como nombres de parámetros.
        avoid_types_as_parameter_names: true

        # Evite el uso de bibliotecas solo web fuera de los paquetes de complementos web de Flutter.
        avoid_web_libraries_in_flutter: true
        
        # Only reference in scope identifiers in doc comments.
        comment_references: true

        # Evita meter bucles en los bloques finally
        control_flow_in_finally: true

        # Evite declaraciones vacias
        empty_statements: true

        # No usar mas de un caso con el mismo valor en switch case
        no_duplicate_case_values: true

        # No use el tipo Null, a menos que esté seguro de que no quiere void.
        test_types_in_equals: true

        # Evita usar un throw en un finally
        throw_in_finally: true

        # Evite el uso de declaraciones innecesarias.
        unnecessary_statements: true

        # Utilice una sintaxis de expresión regular válida.
        valid_regexps: true

        # Evite las API HTML inseguras.
        unsafe_html: true
        '''

    BINDINGS = bindings_code()

    CONTROLLER = controller_code()

    HOMEPAGE = home_page_code()

    APPPAGES = app_pages_code()

    APPROUTES = app_routes_code()

    MAIN = main_code()

    LINTER = linter_code()

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

            linter_for_dart(textWrite=LINTER)

            # Modifica el metodo main
            mainModification()

    except OSError as error:
        print(error)


if __name__ == "__main__":
    main_code()
