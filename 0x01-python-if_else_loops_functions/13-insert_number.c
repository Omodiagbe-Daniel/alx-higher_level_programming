#include "lists.h"

/**
* *insert_node - inserts a number into a sorted singly linked list
* @head: pointer to pointer
* @number: value
* Return: the address of the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;

	if (*head == NULL || head == NULL)
	{
		return (NULL);
	}
	node = malloc(sizeof(listint_t));
	if (!node)
	{
		free(node);
		return (NULL);
	}
	node->n = number;
	tmp = *head;
	while (tmp->next != NULL)
	{
		if ((tmp->next->n > node->n && tmp->n < node->n)
			|| node->n == tmp->n)
		{
			node->next = tmp->next;
			tmp->next = node;
			return (node);
		}
		tmp = tmp->next;
	}
	node->next = tmp->next;
	tmp->next = node;
	return (node);
}
