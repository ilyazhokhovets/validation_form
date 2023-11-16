 const cases = [
     // Сначала идут тесты для существующих шаблонов

     // Полное совпадение полей и типов
    {
        lead_email: 'hot-lead@mail.ru',
        lead_phone: '+7 999 314 15 51',
    },

     // Совпадение полей и типов для существующих полей + поле, которого нет.
     // Так же используется один из двух типов даты
     {
         delivery_date: '2020-12-25',
         courier_phone: '+7 333 242 24 42',
         additional_info: "Santa Claus is coming down the chimney"
     },

     // Использоваие другого типа даты.
     // Также используется поле с именем name, значение которого отличается от поля name в совпадающем шаблоне,
     // однако
     {
         soft_skills: "Creative thinking, Positivity, Adaptability ",
         user_phone: "+7 963 314 15 51",
         user_email: "zhokhovets@mail.ru",
         birthday: "24.12.1997",
         tg: 'john_hovec',
         name: 'Ilya'
     },

     // Далее идут данные, для которых не найдется шаблона

     // Неверный формат телефона
    {
        CEO_email: "ceo1337@group.by",
        CEO_phone: "8 963 314 15 51"
    },

     // Опечатка в поле birth_day, и как следствие отсутствие нужного поля. При этом тип даты корректен
     {
         soft_skills: "Creative thinking, Positivity, Adaptability ",
         user_phone: "+7 963 314 15 51",
         user_email: "zhokhovets@mail.ru",
         birth_day: "24.12.1997",
     },

     // Несуществующая дата
     {
         delivery_date: '2021-02-29',
         courier_phone: '+7 333 242 24 42',
         additional_info: "Santa Claus is coming down the chimney"
     },

     // Неверный формат даты
     {
         delivery_date: '01.01.99',
         courier_phone: '+7 333 242 24 42',
         additional_info: "Santa Claus is coming down the chimney"
     },

     // Перепутаны поля и типы
     {
         lead_phone: 'hot-lead@mail.ru',
         lead_email: '+7 999 314 15 51',
     },

     // Все поля не совпадают
     {
         dummy_field: 'dummy@gmail.com',
         dummy_phone: '+7 999 314 15 51',
     },

     // Некорректный формат почты
     {
         student_email: 'johnny_bbc@@gmail.com',
         student_name: 'Johnny',
     },
 ];


const url = 'http://127.0.0.1:5000/get_form';


cases.forEach(elem => {

  const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(elem),
};

fetch(url, options)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log();
    console.log('request:', elem);
    console.log('response:', data);
    console.log();
  })
  .catch(error => {
    console.error('Fetch error:', error, elem);
  });
})