#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: Pointer to the head of the linked list
* Return: 1 if palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *second_half = NULL, *mid_node = NULL;
	int isPalindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;

	listint_t *prev = NULL, *current = second_half, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	second_half = prev;

	listint_t *first_half = *head;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			isPalindrome = 0;
			break;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	prev = NULL;
	current = prev_slow;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	prev_slow->next = prev;

	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}

	return (isPalindrome);
}
