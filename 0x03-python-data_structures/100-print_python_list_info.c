#include <Python.h>

void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;

    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *element = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}
