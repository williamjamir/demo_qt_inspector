
========================
Qt Style Sheet Inspector
========================

.. image:: https://img.shields.io/travis/ESSS/qt_style_sheet_inspector.svg
        :target: https://travis-ci.org/ESSS/qt_style_sheet_inspector


A inspector widget to view and modify style sheet of a Qt app in runtime.

The inspector check style sheets that was applied to the QApplication, since it's the topmost and any change here can be propagated to all child's

Usage
-----

In order to use the inspector widget on your application, it's necessary to initialize the class `style_sheet_inspector_class` passing the instance of the QMainWindow of your application.

The repository _demo_qt_inspector contains a full example of a Qt Application with an inspector widget being called by a shortcut action.

.. _demo_qt_inspector: https://github.com/williamjamir/demo_qt_inspector

See the demo in action below.




* Free software: MIT license


Observation
-----------

It need PyQt5 to work but it doesn't have it as a dependency, as testing with PyQt5 pypi proved
unreliable (may be changed in the future).


Features
--------

* Can view current style sheet of application during runtime
* Style sheet can be changed in runtime, facilitating the process of designing a custom GUI
* Has a search bar to help find specific types or names
* Can undo/redo changes
