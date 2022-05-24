import PySimpleGUI as Sg
from weather_api import WeatherInfo


USER_CITY = 'Delhi'
API_KEY = '<API_KEY>'
USER_FONT = "Roboto"


def main():
    Sg.theme('DarkGrey11')

    weather_info = WeatherInfo(city_name=USER_CITY,
                               api_key=API_KEY,
                               units='metric')
    weather_details = weather_info.get_weather_info()
    user_weather = weather_details[0]
    user_temperature = weather_details[1]

    layout = [[Sg.Text(USER_CITY, font=f"{USER_FONT} 30")],
              [
                  Sg.Text(user_weather, font=f"{USER_FONT} 100"),
                  Sg.Text(f' {user_temperature}℃ ', font=f"{USER_FONT} 50")
               ]
              ]

    # Create the Window
    window = Sg.Window('Weather App', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    main()
