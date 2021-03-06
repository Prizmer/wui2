# coding -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prizmer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^config/$', views.choose_service), # Выберите отчет
    url(r'^service_file/$', views.service_file), # форма для загрузки файла на сервер
    url(r'^service_file_loading/$', views.service_file_loading), # загрузка файла на сервер
    url(r'^service_electric/$', views.service_electric), # электрика, загрузка нужных полей
    url(r'^service_electric_load/$', views.service_electric_load), # электрика прогрузка
    url(r'^load_tcp_ip/$', views.load_port), # загрузка портов по элетрике
    url(r'^make_sheet/$', views.MakeSheet), #возвращает список страниц в книге excel
    url(r'^load_electric_objects/$', views.load_electric_objects), # загрузка объектов и абонентов
    url(r'^load_electric_counters/$', views.load_electric_counters), # загрузка счётчиков
#    url(r'^electric/$', views.electric),
    url(r'^service_water/$', views.service_water), # электрика, загрузка нужных полей
    url(r'^load_water_objects/$', views.load_water_objects), # вода, загрузка нужных полей
    url(r'^load_water_pulsar/$', views.load_water_pulsar), # вода, загрузка пульсаров и создание связей с абонентами
    url(r'^load_water_port/$', views.load_water_port), # загрузка портов из файла для воды
    
    url(r'^service_change_electric/$', views.change_meters_v2), # замена одного счётчика на другой
    url(r'^service_replace_electric/$', views.replace_electric_meters_v2), # поменять местами счётчики
    url(r'^service_get_info/$', views.get_info), # 
    url(r'^get_electric_progruz/$', views.get_electric_progruz), # прогрузочная ведомость в эксель
    url(r'^get_electric_progruz_com/$', views.get_electric_progruz_com), # прогрузочная ведомость в эксель по com-порту
    url(r'^get_water_progruz/$', views.get_water_progruz), # прогрузочная ведомость в эксель
    url(r'^get_water_impulse_progruz/$', views.get_water_impulse_progruz), # прогрузочная ведомость в эксель
    url(r'^get_heat_progruz/$', views.get_heat_progruz), # прогрузочная ведомость в эксель
    url(r'^load_balance_group/$', views.load_balance_group), # загрузка портов по электрике
    url(r'^service_balance_load/$', views.service_balance_load), #загрузка формы для прогрузки балансных групп

    url(r'^add_current_taken_params_pulsar16m/$', views.add_current_taken_params_pulsar16m), #загрузка формы для прогрузки балансных групп
    url(r'^get_electric_template/$', views.get_electric_template), #возвращает excel форму образец для прогрузочной ведомости
    url(r'^get_heat_template/$', views.get_heat_template), #возвращает excel форму образец для прогрузочной ведомости
    url(r'^get_water_digital_template/$', views.get_water_digital_template), #возвращает excel форму образец для прогрузочной ведомости
    url(r'^get_water_impulse_template/$', views.get_water_impulse_template), #возвращает excel форму образец для прогрузочной ведомости
    url(r'^get_balance_template/$', views.get_balance_template), #возвращает excel форму образец для прогрузочной ведомости
    
    url(r'^service_load30_page/$', views.service_load30_page), # загрузка страницы
    url(r'^service_load30/$', views.service_load30), # загрузка получасовок в базу из html

    url(r'^service_user_account/$', views.service_user_account), # страница для добавления пользователей личного кабинета
    url(r'^load_user_account/$', views.load_user_account), # добавление аккаунтов пользователей личного кабинета
    url(r'^get_users_account_template/$', views.get_users_account_template), #возвращает excel форму образец для прогрузочной ведомости get_users_account_template
    url(r'^service_del_meters/$', views.service_del_meters), # удаление приборов через прогрузочную ведомость

    url(r'^load_80020_group/$', views.load_80020_group), # удаление приборов через прогрузочную ведомость
    url(r'^get_80020_template/$', views.get_80020_template), #возвращает excel форму образец для прогрузочной ведомости
    
    url(r'^del_meters/$', views.del_meters), #Удаление приборов из БД по прогрузочной ведомости
)
