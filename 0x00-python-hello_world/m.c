#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list);

int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    /********** Test Case 1: Linked list with no loop **********/
    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    print_listint(head);
	
    printf("case 1 = \n");
    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    free_listint(head);
    head = NULL;

    /********** Test Case 2: Linked list with loop **********/
    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    current = head;
    for (i = 0; i < 3; i++)
        current = current->next;
    temp = current->next;
    current->next = head;
	printf("case 2 = \n");
    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 3; i++)
        current = current->next;
    current->next = temp;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    free_listint(head);
    head = NULL;
    /********** Test Case 3: Empty list **********/
    printf("case 3 = \n");
    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");
    /********** Test Case 4: 1 item in list, no loop **********/
    head = NULL;
    add_nodeint(&head, 0);
	
    printf("case 4 = \n");
    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    free_listint(head);
    head = NULL;
    /********** Test Case 5: 1 item in list, with loop *********/
    head = NULL;
    add_nodeint(&head, 0);
    head->next = head;
    printf("case 5 = \n");
    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");
	
    free(head);
    head = NULL;

    /********** Test Case 6: 2 items in list, no loop **********/
    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
	
    printf("case 6 = \n");
    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    free_listint(head);
    return 0;
}
