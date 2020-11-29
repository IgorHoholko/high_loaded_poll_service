
import telepot




def main():
    token = '1214785858:AAH1UcQrTa2sqFspGRXrAqhdMzOgr_FHoAs'
    TelegramBot = telepot.Bot(token)

    print( TelegramBot.getMe() )
    print(TelegramBot.getUpdates())


if __name__ == '__main__':
    main()
