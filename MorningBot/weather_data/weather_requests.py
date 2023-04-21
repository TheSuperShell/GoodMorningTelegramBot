import requests

code_to_emoji = {
	"Clear": "Ясно \U00002600",
	"Clouds": "Облачно \U00002601",
	"Rain": "Дождь \U00002614",
	"Drizzle": "Дождь \U00002614",
	"Thunderstorm": "Гроза \U000026A1",
	"Snow": "Снег \U0001F328",
	"Mist": "Туман \U0001F32B"
}


def get_weather(city, weather_api):
	try:
		r = requests.get(
			f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric'
		)
		data = r.json()
		weather = data['weather'][0]['main']
		weather_string = code_to_emoji[weather] if weather in code_to_emoji else ''
		cur_temp = data['main']['temp']
		feels_like = data['main']['feels_like']
		humidity = data['main']['humidity']
		pressure = data['main']['pressure']
		wind = data['wind']['speed']
		results = (
			f'Прогноз погоды на день:\n\n'
			f'Температура: {cur_temp:.0f} C°, {weather_string}\n'
			f'Ощущается как {feels_like:.0f} C°\n'
			f'Влажность: {humidity}%\n'
			f'Давление: {pressure * 0.75:.0f} мм.рт.ст.\n'
			f'Скорость ветра: {wind} м/с'
		)
		return results
	except Exception as e:
		print(e)
		return 'Ошибка!'
