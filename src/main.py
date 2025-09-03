from classes.agenda import Agenda
from classes.contatoPessoal import ContatoPessoal
from classes.contatoProfissional import ContatoProfissional

if __name__ == "__main__":
    agenda = Agenda()

    pessoal = ContatoPessoal("Ariel", "79998432127", "Amigo")
    pro = ContatoProfissional("Felipe", "79940028922", "felipe@gmail.com")

    agenda.adicionarContato(pessoal)
    agenda.adicionarContato(pro)

    print("\n--- Agenda Inicial ---")
    agenda.imprimirAgenda()

    agenda.removerContato("felipe")

    print("\n--- Agenda Após Remover Felipe ---")
    agenda.imprimirAgenda()
