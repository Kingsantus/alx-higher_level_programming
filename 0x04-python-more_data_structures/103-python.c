#include <stdio.h>
#include <Python.h>
#include <bytesobject.h>

/**
 * print_python_list: takes a PyObject pointer as input
 * PyList_Check. If it's not, an error message is printed
 * PyObject_GetItem to retrieve the element at the given index
 * Py_DECREF to ensure proper memory management.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyObject_Length(p);

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyObject_GetItem(p, PyLong_FromSsize_t(i));
		const char *elementType = Py_TYPE(element)->tp_name;

		printf("Element %ld: %s\n", i, elementType);
		Py_DECREF(element);
	}
}

/**
 * print_python_bytes: function takes a PyObject pointer as input
 * PyBytes_Check check If it's not, an error message is printed
 * PyObject_Size retrieves its size 
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytesObj = (PyBytesObject *)p;
	Py_ssize_t size;
	char *data = bytesObj->ob_sval;
	Py_ssize_t maxBytes;

	maxBytes = (size > 10) ? 10 : size;
	size = PyObject_Size(p);

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  Size: %ld\n", size);
	printf("  Address of the object: %p\n", (void *)p);
	printf("  Bytes: ");

	for (Py_ssize_t i = 0; i < maxBytes; i++)
	{
		printf("%02hhx", data[i]);
		if (i < maxBytes - 1)
		{
			printf(" ");
		}
	}

	printf("\n");
}
