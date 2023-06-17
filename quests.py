from typing import Final

TOKEN: Final = 'seu token'
BOT_USERNAME: Final = '@seu_username'

#-----------------------------------------------------------------

parte_1 = "Nesta parte, estamos importando as bibliotecas e módulos necessários para o funcionamento do bot. 'quests' é um módulo externo que contém a variável 'codigo_seco', que será usada posteriormente. Também importamos as classes 'Update' da biblioteca 'telegram' e 'Application, CommandHandler, MessageHandler, filters e ContextTypes' da biblioteca 'telegram.ext'. Para instalar a biblioteca do telegram, use: pip install python_telegram_bot. Além disso preste atenção nas importações e criação do módulo externo 'quests', pois ele vai conter grande parte das variáveis necessárias para o funcionamento do bot."

#-----------------------------------------------------------------

parte_2 = "A função 'start_command' é um manipulador para o comando /start. Quando o usuário envia esse comando, o bot responde com uma mensagem de boas-vindas e fornece algumas instruções sobre como obter o código completo e obter mais detalhes sobre ele. A função 'help_command' é um manipulador para o comando /help. Quando o usuário envia esse comando, o bot responde com uma mensagem contendo informações sobre os comandos disponíveis, neste caso, /start e /help. A função 'custom_command' é um manipulador para um comando personalizado. Quando o usuário envia esse comando, o bot responde com uma mensagem predefinida, informando que é um comando personalizado e que o usuário pode adicionar o texto que desejar nesse comando."

#-----------------------------------------------------------------

parte_3 = "a função 'handle_response' executará a lógica de resposta do bot com base no texto que o usuário enviar. Ela verifica se o texto contém palavras-chave específicas e retorna a resposta apropriada. Aqui armazenamos as respostas em variáveis no módulo 'quests.py', que deve estar localizado no mesmo diretório que nosso código. Para armazenar o código todo, ao qual eu chamei de 'código seco', eu utilizei um 'arquivo.txt' e criei um 'with' com um modo 'r', atribuindo o conteúdo a uma variável 'codigo_seco'. Com o restante das responstas eu só determinei variáveis atribuindo textos."

#-----------------------------------------------------------------

parte_4 = "Agora, vamos definir a função 'handle_message', que será responsável por lidar com as mensagens recebidas pelo bot. Ela extrai informações básicas da mensagem, como o tipo de chat e o texto enviado pelo usuário. Em seguida, chama a função 'handle_response' para obter a resposta apropriada com base no texto recebido. Aqui temos uma interação entre mensagens recebidas e a resposta adequada por meio do 'handle'. Em seguida, temos a função error, que lida com possíveis erros que possam ocorrer durante a execução do bot. Ela imprime informações sobre o erro no console."

#-----------------------------------------------------------------

parte_5 = "Agora, vamos para a parte de execução do programa. Verificamos se o script está sendo executado diretamente e não sendo importado como um módulo (ele é executado no escopo global, o que significa que todas as variáveis, funções e classes definidas no script ficam disponíveis globalmente. No entanto, quando você importa um script Python como um módulo em outro script, o código do módulo é executado apenas uma vez, no momento da importação). Em seguida, construímos um objeto 'Application' passando o token do bot como parâmetro (o token foi definido em uma variável em quests.py), que é usado para autenticar o bot no Telegram. Agora, adicionamos os manipuladores (handlers) aos comandos e mensagens que o bot deve responder. No caso, adicionamos três manipuladores para os comandos '/start, /help e /custom', e um manipulador para as mensagens de texto. Também adicionamos um manipulador de erro. Por fim, iniciamos a execução do bot usando o método 'run_polling', que verifica periodicamente o servidor do Telegram em busca de novas mensagens."

#-----------------------------------------------------------------