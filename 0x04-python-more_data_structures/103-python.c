#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_bytes - Print bytes info
 * @p: python object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, gov;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size >= 10)
		gov = 10;
	else
		gov = size + 1;

	printf("  first %ld bytes:", gov);

	for (i = 0; i < gov; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
 * print_python_list - Print list info
 * @p: python object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size, n;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (n = 0; n < size; n++)
	{
		obj = ((PyListObject *)p)->ob_item[n];
		printf("Element %ld: %s\n", n, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
