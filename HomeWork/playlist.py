class Playlist:
    def __init__(self):
        self.songs = []  # Список песен
        self.current_index = -1  # Индекс текущей песни 
    
    def add_song(self, title, artist):
        self.songs.append({'title': title, 'artist': artist})        # Добавляем песню в конец списка
        
        if self.current_index == -1:        # Если это первая песня, делаем её текущей
            self.current_index = 0
        
        print(f"Добавлена песня: {title} - {artist}")
    
    def remove_song(self, title):
        for i, song in enumerate(self.songs):        # Ищем песню с указанным названием
            if song['title'] == title:
                removed_song = self.songs.pop(i)                # Удаляем песню из списка
                print(f"Удалена песня: {removed_song['title']} - {removed_song['artist']}")
                
                if len(self.songs) == 0:            # Корректируем текущий индекс при необходимости
                    self.current_index = -1                    # Если плейлист стал пустым
                elif i <= self.current_index:
                    self.current_index = max(0, self.current_index - 1)           # Если удалили текущую или предыдущую песню
                return True
        
        print(f"Песня '{title}' не найдена")        # Если песня не найдена
        return False
    
    def shuffle(self):
        import random
        
        if len(self.songs) > 0:
            current_song = self.songs[self.current_index]            # Сохраняем текущую песню
            
            random.shuffle(self.songs)            # Перемешиваем плейлист
            
            for i, song in enumerate(self.songs):  # Находим новую позицию текущей песни
                if song['title'] == current_song['title']:
                    self.current_index = i
                    break
            
            print("Плейлист перемешан!")
    
    def next(self):
        if len(self.songs) > 0:
            self.current_index = (self.current_index + 1) % len(self.songs)            # Переходим к следующему индексу
            print(f"Переключено на: {self.current_song()} - {self.current_artist()}")
    
    def previous(self):
        if len(self.songs) > 0:
            self.current_index = (self.current_index - 1) % len(self.songs)            # Переходим к предыдущему индексу 
            print(f"Переключено на: {self.current_song()} - {self.current_artist()}")
    
    def current_song(self):
        if self.current_index >= 0 and self.current_index < len(self.songs):
            return self.songs[self.current_index]['title']
        return None
    
    def current_artist(self):
        if self.current_index >= 0 and self.current_index < len(self.songs):
            return self.songs[self.current_index]['artist']
        return None
    
    def show_playlist(self):
        if len(self.songs) == 0:
            print("Плейлист пуст")
        else:
            print("\n=== ТЕКУЩИЙ ПЛЕЙЛИСТ ===")
            for i, song in enumerate(self.songs):
                current_mark = " ТЕКУЩАЯ" if i == self.current_index else "" # отметка на текущей песне
                print(f"{i+1}. {song['title']} - {song['artist']}{current_mark}")


if __name__ == "__main__":
    print("___ ДЕМОНСТРАЦИЯ РАБОТЫ ПЛЕЙЛИСТА ___\n")
    
    playlist = Playlist()    # Создаем новый плейлист
    
    playlist.add_song("Bohemian Rhapsody", "Queen")    # Добавляем песни 
    playlist.add_song("Imagine", "John Lennon")
    playlist.add_song("Shape of You", "Ed Sheeran")
    
    print("\n___ Проверка методов согласно примеру ___")
    print(playlist.current_song())    # Выводим текущую песню и исполнителя
    print(playlist.current_artist()) 
    
    playlist.next()    # Переключаем на следующую
    print(playlist.current_song())
    
    playlist.previous()    # Возвращаемся на предыдущую
    print(playlist.current_song()) 
    
    playlist.remove_song("Imagine")    # Удаляем песню и переключаем на следующую
    playlist.next()
    print(playlist.current_song())
    
    print("\n--- Дополнительная демонстрация ---")
    playlist.show_playlist()    # Показываем весь плейлист
    
    playlist.shuffle()    # Перемешиваем плейлист
    playlist.show_playlist()