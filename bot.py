from quests import *
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


# funções que permitem a execução de comandos específicos
# a utilização do 'async' torna possível o processamento das funções em segundo plano na execução do código
# 'await' é utilizada em funções assíncronas no Python para indicar que uma determinada chamada de função ou expressão deve aguardar a conclusão de uma tarefa assíncrona antes de prosseguir com a execução do código
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Seja bem vindo!! Vou te auxiliar na criação do seu bot para o Telegram. \nDigite: (código) para obter o código completo. \nDigite: (ver mais) para mais detalhes sobre o código. \nDigite: (acessar api_key) para aprender a configurar a parte inicial do bot no telegram')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('comando /start: indica a inicialização do bot. \ncomando /help: disponibiliza os comandos do bot. \ncomando /custom: mensagem pré determinada \n\noutros comandos: \ncódigo \ncodigo \nver mais \nparte 1 \nparte 2 \nparte 3 \nparte 4 \nparte 5')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Este é um comando personalizado, você pode adicionar qualquer texto para aparecer ao executar este comando.')



# função que executa uma lógica de respostas baseada no que o usuário irá digitar
def handle_response(text: str) -> str:
    processed: str = text.lower() 

    if 'código' in processed or 'codigo' in processed:
        return 'https://github.com/keedkeior/bot_para_o-_telegram'

    if 'ver mais' in processed:
        return 'Vejo que quer saber um pouco mais sobre o código em questão. Vou te ajudar detalhando cada parte dele, mas tenha o código ao seu lado para trabalharmos juntos!\n \nDigite a parte do código que deseja revisar \nparte 1 \nparte 2 \nparte 3 \nparte 4 \nparte 5'
    
    if 'acessar api_key' in processed:
        return "1- Procure por 'BotFather' no telegram e inicie a conversa. \n2- Após isso ele ira te mandar todos os comandos e funcionalidades. \n3- Use /newbot e dê um nome ao seu bot, após isso dê um username ao seu bot(no usarname é necessário o uso do termo 'bot' no final). \n4- Pegue sua API_KEY e guarde em um lugar seguro. \nNo botfather você edita a descrição do bot, imagem do perfil entre outras coisas disponíveis na lista de comandos, basta usar o username com '@' para dizer qual bot você deseja editar"

    if 'parte 1' in processed:
        return parte_1
    
    if 'parte 2' in processed:
        return parte_2
    
    if 'parte 3' in processed:
        return parte_3
    
    if 'parte 4' in processed:
        return parte_4
    
    if 'parte 5' in processed:
        return parte_5

    return 'Desculpe, solicite sua pretenção com mais clareza!'


# Esses parâmetros fornecem informações sobre a mensagem recebida e o contexto da aplicação.
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # extraem informações básicas da mensagem recebida. message_type recebe o tipo de chat em que a mensagem foi enviada
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # imprime um log para fins de depuração, exibindo o ID do usuário, o tipo de chat e o texto da mensagem.
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # usado para fazer interação entre conversas em um grupo (por meio da menção ao bot)
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  # não irá responder caso o bot não seja mencionado
    else:
        response: str = handle_response(text)

    # imprime a resposta do bot no console e enviam a resposta de volta ao remetente da mensagem.
    print('Bot:', response)
    await update.message.reply_text(response)

# Log de erros
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



# execução do programa

# verifica se o script está sendo executado diretamente e não sendo importado como um módulo
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build() #constrói um objeto da aplicação definindo o token que identifica o seu bot no Telegram

    # Comandos (adicionam manipuladores (handlers) para lidar com comandos específicos do bot.)
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Mensagens (adiciona um manipulador para lidar com mensagens de texto)
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log de erros (adiciona um manipulador de erro para lidar com exceções ocorridas durante a execução do bot)
    app.add_error_handler(error)

    print('Em processo...') # execução do bot
    

    app.run_polling(poll_interval=5) #verifica periodicamente o servidor do Telegram em busca de novas mensagens no intervalo de tempo em segundos (5)