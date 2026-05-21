from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama


load_dotenv()


def main():
    print("Hello from file-1!")
    information = """Tatiana Lobo Coelho de Sampaio (Rio de Janeiro, 4 de outubro de 1966) é uma bióloga e professora brasileira da Universidade Federal do Rio de Janeiro.

Sampaio recebeu projeção nacional por suas pesquisa acerca da polilaminina, uma molécula que apresentou potencial para reverter lesões medulares e que, no ano de 2026, foi aprovada pela Anvisa para iniciar a etapa de testes clínicos.[1] A polilaminina foi comparada à fosfoetanolamina, devido ao hype promovido por Sampaio em suas entrevistas sobre o composto e à ausência de estudos que comprovem sua eficácia em humanos.[2] Alicia Kowaltowski alertou que a "torcida antecipada" era perigosa ao desviar os esforços de estudos embasados.[3]
Carreira

Nascida em Vila Isabel, na zona norte do Rio de Janeiro, Tatiana Sampaio é filha de Luiz Sérgio Coelho de Sampaio, engenheiro, economista e filósofo brasileiro, e de Lailce Regina Lobo de Sampaio, tendo desejado desde a infância ser cientista cientista.[4][5] No colégio, se interessou por Biologia, mas sempre manteve o gosto pela pesquisa.[5]

Em 1983, iniciou a gradução em Ciências Biológicas pela Universidade Federal do Rio de Janeiro (UFRJ), tendo concluído o bacharelado em 1986. No ano seguinte, 1987, iniciou o mestrado em Ciências Biológicas pela mesma universidade e foi orientada pelo Dr. Adalberto Ramón Vieyra, obtendo o título de Mestre em 1990.

Ainda em 1990, iniciou seu doutorado em Ciências, a ser orientada novamente pelo Dr. Adalberto Ramon Vieyra, doutorando-se pela UFRJ em 1992.

Em 1992, iniciou seu primeiro pós-doutorado pela Universidade de Illinois, Estados Unidos da América, em Bioquímica (Química de Macromoléculas), com especialização em Proteínas, tendo-o concluído em 1994.[6]

No ano seguinte, 1995, aos 27 anos, depois do pós-doutorado, Sampaio ingressou na UFRJ como professora.[6] Dois anos depois, em 1997, iniciou seus estudos sobre a polilaminina.[5][7]

Fez, ainda, um segundo pós-doutorado entre 1999 e 2000 pela Universidade de Erlangen-Nuremberga, Alemanha.[6]

Atualmente, é coordenadora do Laboratório de Biologia da Matriz Extracelular do Instituto de Ciências Biomédicas da UFRJ, um laboratório de pesquisa de bioquímica e biofísica de proteínas, mais especificamente a polilaminina.[5][7] Esses estudos indicam que a substância tem potencial para reverter lesões da medula espinhal.[1]

A polilaminina é uma versão da laminina recriada em laboratório.[8] Como resultado das pesquisas de Sampaio, a Agência Nacional de Vigilância Sanitária (Anvisa) autorizou a realização da fase 1 de estudos clínicos com a substância.[7]Serão avaliadas de 20 a 80 pessoas, com os objetivos de determinar a farmacocinética, a farmacodinâmica, a confiança e a segurança da substância em indivíduos saudáveis, além das estimativas de doses e efeitos.[9] Nesta estapa, cinco pessoas com lesão medular completa receberão dose única da polilaminina até 48 horas após o trauma. Os pacientes serão acompanhados por seis meses para avaliar a ocorrência de reações adversas graves.[7]
Vida pessoal

Tatiana Sampaio tem três filhos. Sua casa é um lugar por onde alunos, sobrinhos e amigos dos filhos circulam com frequência.[5]

    Ela diz que, nessa trajetória, não enfrentou barreiras profissionais por ser uma cientista mulher. "Na área biomédica somos maioria há muito tempo. O desafio não é representatividade, é conciliar vida pessoal e trabalho."[5]

Ela não tem religião. Mas acredita em Deus e que a ciência não é dona de toda verdade. Para ela: As verdades da ciência são úteis, mas parciais. O ser humano é mais do que um corpo.
    """
    summary_template = """
 given the information {information} about a person I want you to create:
 1. a short summary
 2.two interesting facts about them
 """
    summary_prompt_template = PromptTemplate(template=summary_template, 
    input_variables=["information"])
    # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information}) 
    print(response.content)
if __name__ == "__main__":
    main()
