from vkbottle import Keyboard, Text, BaseStateGroup
from vkbottle.bot import Bot, Message
import os

bot = Bot(os.environ['TOKEN'])

class States(BaseStateGroup):
    CHOOSE_STATE = 0
    ANYTHINGELSE_STAGE = 1
    STOP_STATE = 2

@bot.on.message(text="Начать")
async def start(message: Message):
    await message.answer("Привет! Это бот 1NFORM. Я помогу" + 
                        " тебе не запутаться в отделах проекта" + 
                        " и заполнить форму регистрации. Для начала" +
                        " выбери отдел, в который хочешь отправить заявку.")
    await bot.state_dispenser.set(message.peer_id, States.CHOOSE_STATE)
    await choosewishely(message.peer_id)

async def choosewishely(peer_id):
    await bot.state_dispenser.set(peer_id, States.CHOOSE_STATE)
    keyboard = Keyboard(one_time = True, inline=False)
    keyboard.add(Text("Design-отдел"))
    keyboard.add(Text("Media-отдел"))
    keyboard.add(Text("Event-отдел"))
    keyboard.row()
    keyboard.add(Text("Отдел Модерации"))
    keyboard.add(Text("Отдел Собеседников"))
    keyboard.row()
    keyboard.add(Text("Отдел Консультации"))
    keyboard.add(Text("Отдел Серферов"))
    keyboard.row()
    keyboard.add(Text("Отдел Информатизации"))
    keyboard.row()
    keyboard.add(Text("Отдел Маркетинга и Рекламы"))
    await bot.api.messages.send(peer_id=peer_id,message="В какой отдел ты хочешь?", keyboard=keyboard.get_json(), random_id=0)

@bot.on.message(state=States.CHOOSE_STATE, text="Отдел Информатизации")
async def info(message: Message):
    await message.answer("Люди, которые создают сайты, ботов и другие сервисы" +
                        " и системы, облегчая работу не только организаторам" +
                        " проекта, но и администрации вуза. Например, бот, который" + 
                        " сейчас присылает тебе эти сообщения, был сделан нашими программистами.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Информатизация")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Отдел Модерации")
async def moder(message: Message):
    await message.answer("Отдел Модерации работает с организаторами проекта 1NFORM." +
                        " Модераторы выстраивают позиционирование нашей команды: следят" +
                        " за соблюдением правил и регламента, а также модерируют контент" + 
                        " в социальных сетях проекта. Перед началом активной фазы сотрудники" + 
                        " отдела проводят доскональную проверку всех социальных сетей каждого организатора проекта.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Модерация")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Отдел Собеседников")
async def sobes(message: Message):
    await message.answer("Люди, которые отвечают за беседы факультетов и беседы по интересам." +
                        " Они знают все об университете и котиках. В обязанности собеседников" +
                        " входит общение с первокурсниками в беседах, модерирование чатов и готовность" +
                        " ответить на любой вопрос, касающийся обучения и не только.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Собеседник")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Design-отдел")
async def dezign(message: Message):
    await message.answer("Разрабатывают фирменный стиль и айдентику, а также мерч для мероприятий" +
                        " и организаторов проекта. Во время работы у дизайнеров есть возможность не" +
                        " только отточить свои навыки, создавая шаблонные посты, но и проявить креативность," +
                        " генерируя развлекательный контент.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Design")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Отдел Маркетинга и Рекламы")
async def omir(message: Message):
    await message.answer("Ведет интернет-ресурсы и занимается продвижением проекта в социальных сетях." +
                        " Одной из главных задач отдела является повышение узнаваемости проекта не" +
                        " только в стенах университета, но и за его пределами. Где ты мог(ла) познакомиться" +
                        " с ними? В группах 1NFORM, Абитуриенты/Первокурсники СПбГУТ, НеНочная во ВКонтакте," +
                        " а также на платформе Яндекс.Дзен.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/ОМиР")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Отдел Консультации")
async def cons(message: Message):
    await message.answer("Кто встречает тебя в приемной комиссии и отвечает тебе в социальных сетях?" +
                        " Конечно же, консультанты. Их задача – помочь абитуриентам с выбором факультета" +
                        " или направления обучения и объяснить все страшное простыми словами. " +
                        "Консультанты знают ответы на все: от стоимости проезда в метро до всех нюансов подачи документов.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Консультация")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Отдел Серферов")
async def surf(message: Message):
    await message.answer("Первые из студентов, с кем ты общаешься, когда поступаешь в наш университет." +
                        " Серферы занимаются мониторингом приказов о поступлении и поиском новоиспеченных" +
                        " первокурсников в социальных сетях. Порой это бывает непросто, ведь никогда не знаешь," +
                        " кто скрывается за аватаркой с котиком. После нахождения нужного человека серфер" +
                        " направляет его в беседу факультета.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Серферы")
    await anythingElse(message.peer_id)
    
@bot.on.message(state=States.CHOOSE_STATE, text="Media-отдел")
async def media(message: Message):
    await message.answer("Снимают фото- и видеоконтент для социальных сетей проекта и его внешнего представления" +
                        " на других площадках. Увидеть результаты работы Media-отдела ты можешь в подборках" +
                        " фотографий Бонча в группе Первокурсников, на знаменитых аватарках организаторов" +
                        " проекта и в подкасте «Точка зрения| РОV».\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Media")
    await anythingElse(message.peer_id)

@bot.on.message(state=States.CHOOSE_STATE, text="Event-отдел")
async def event(message: Message):
    await message.answer("На Event-отделе лежит ответственность представить первокурсникам другую сторону" +
                        " студенческой жизни. Они проводят первое мероприятие для поступивших ребят, где" +
                        " знакомят их друг с другом и с университетом. Но не стоит думать, что на этом" +
                        " их работа заканчивается. Во время пассивной фазы Event-отдел организует мероприятия," +
                        " направленные на командообразование, развитие проекта и организаторов.\n" + 
                        "\nПодать заявку в отдел можно тут:\nhttps://ъыъ.рф/Event")
    await anythingElse(message.peer_id)

async def anythingElse(peer_id):
    await bot.state_dispenser.set(peer_id, States.ANYTHINGELSE_STAGE)
    keyboard = Keyboard(one_time=True, inline=False)
    keyboard.add(Text("Да"))
    keyboard.add(Text("Нет"))
    await bot.api.messages.send(peer_id=peer_id,message="Желаешь вступить куда-нибудь еще?", keyboard=keyboard.get_json(), random_id=0)

@bot.on.message(state=States.ANYTHINGELSE_STAGE, text="Да")
async def yos(message: Message):
    await choosewishely(message.peer_id)

@bot.on.message(state=States.ANYTHINGELSE_STAGE, text="Нет")
async def no(message: Message):
    await message.answer("Спасибо за заявку! Ждём тебя на следующих этапах отбора 🤍\n\n P.s.: чтобы запустить меня заново,напиши «Начать»")
    # await bot.state_dispenser.set(message.peer_id, state=None)
    return
    

if __name__ == '__main__':
    bot.run_forever()