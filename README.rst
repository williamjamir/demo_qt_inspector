
========================
Demo for Qt Style Sheet Inspector
========================

This is a demo application for the qt_style_sheet_inspector_, a lib that enables qt application to modify style sheet in runtime.

.. _qt_style_sheet_inspector: https://github.com/ESSS/qt_style_sheet_inspector

Usage
-----

In order to use the inspector widget on your application, it's necessary to initialize the class :code:`style_sheet_inspector_class` passing the instance of the :code:`QMainWindow` from the application.

See the demo in action:

.. image:: https://github.com/williamjamir/demo_qt_inspector/blob/master/images/qt_inspector_demo.gif
    :width: 10px
    :height: 10px
    :scale: 10 %



Features
--------
view current style sheet of application during runtime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The inspector only checks for style sheets that was applied to the QApplication, it's the topmost and any change here can be propagated to all child's. 
    
        Style sheets that applied to an individual widget will not appers on the inspector.


Style sheet can be changed in runtime (Pressing CTRL+S)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. image::  https://github.com/williamjamir/demo_qt_inspector/blob/master/images/qt_inspector_runtime_changes.gif
        :width: 10px
        :height: 10px
        :scale: 10 %

Search bar to help find specific types or names (Pressing F3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    .. image:: https://github.com/williamjamir/demo_qt_inspector/blob/master/images/qt_inspector_search.gif
        :width: 10px
        :height: 10px
        :scale: 10 %

Can undo/redo changes (Pressing CTRL+ALT+Z or CTRL+ALT+Y)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       
    .. image:: https://github.com/williamjamir/demo_qt_inspector/blob/master/images/qt_inspector_undo_redo.gif
        :width: 10px
        :height: 10px
        :scale: 10 %
    


Observation
-----------

    It need PyQt5 to work but it doesn't have it as a dependency.
    

* Free software: MIT license
