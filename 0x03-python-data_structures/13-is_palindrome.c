#include "lists.h"


/**
*list_len -  A function that compute the lenght of a list
*@head: the head of the list
*Return: The lenght of the list
*/

void reverse(listint_t **head)
{
	listint_t *prev = NULL, *curr, *next = NULL;

	curr = *head;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	(*head) = prev;
}


int compare_element(listint_t **head1, listint_t **head2)
{
	listint_t *tmp1 = *head1, *tmp2 = *head2;

	while (tmp1 && tmp2)
	{
		if (tmp1->n == tmp2->n)
		{
			return (1);
		}
		return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}
	return (0);
}



int is_palindrome(listint_t **head)
{
	listint_t *fast_ptr = *head, *slow_ptr = *head, *prev_to_slow = NULL,
	*second_half, *mid_node;

	while (fast_ptr && fast_ptr->next)
	{
		fast_ptr = fast_ptr->next->next;
		prev_to_slow = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr)
	{
		mid_node = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	second_half = slow_ptr;
	prev_to_slow = NULL;

	reverse(&second_half);

	int comp = compare_element(head, &second_half);

	if (mid_node != NULL) 
	{ 
		prev_to_slow->next = mid_node; 
		mid_node->next = second_half; 
	} 
	else
	{
		prev_to_slow->next = second_half; 
	}
	return (comp);
}
