##
## EPITECH PROJECT, 2023
## neural
## File description:
## Makefile
##

NAME	= 	my_torch

SRC		=	mytorch.py

CP			=	cp

CHMOD		=	chmod

EXEC_RIGHTS	=	+x

RM			=	rm -rf

all: $(NAME)

$(NAME):
	$(CP) $(SRC) $(NAME)
	$(CHMOD) $(EXEC_RIGHTS) $(NAME)

tests_run: all

	$(CHMOD) $(EXEC_RIGHTS)

clean:
	$(RM) .pytest_cache/

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re