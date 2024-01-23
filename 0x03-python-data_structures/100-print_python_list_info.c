#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: PyObject list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, space, x;
	PyObject *ob;

	size = Py_SIZE(p);
	space = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", space);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		ob = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
