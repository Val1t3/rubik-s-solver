##
## EPITECH PROJECT, 2023
## Resolv-Rubik's
## File description:
## Makefile
##

D_SRC	=	./src/

NAME	=	rubiks-resolver

$(NAME): $(wildcard $(D_SRC)*.py)
		cp $(D_SRC)main.py $@
		chmod +x $@

all: $(NAME)

clean:
	rm -f $(NAME)
	rm -f $(NAME).exe

fclean: clean

re: fclean all

.PHONY: all clean fclean re