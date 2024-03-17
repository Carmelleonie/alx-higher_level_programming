#include <stdio.h>
#include <Python.h>
void print_python_list_info(PyObject *p)
{
	int size_of_list, allocated_memory, i;
	PyObject *list;

	size_of_list = PyList_Size(p);
	allocated_memory = Py_SIZE(p);
	printf("[*] Size of the Python List = %d", size_of_list);
	printf("[*] Allocated = %d", allocated_memory);
	for (i = 0; i < size_of_list; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name); 
	}
}
