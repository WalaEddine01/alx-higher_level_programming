#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints basic info about python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int a, b, i;
	PyObject *obj;

	a = Py_SIZE(p);
	b = ((PylistObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", a);
	printf("[*] Allocated = %d\n", b);

	for (i = 0; i < a; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
