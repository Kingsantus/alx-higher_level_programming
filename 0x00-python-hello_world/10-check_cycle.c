#include "lists.h"
#include <stdio.h>

/**
* check_circle(): uses param listint list
* @list: point to the node
* loop to ensure single linked list in both second and head
*
* Return: 1 successful and 0 unsuccessful
*/
int check_cycle(listint_t *list)
{
	listint_t *second, *head;

	if (!list || !list->next)
		return (0);

	head = list;
	second = list->next;
	while (second && head && second->next)
	{
		if (second == head)
			return (1);
		second = second->next->next;
		head = head->next;
	}
	return (0);
}
