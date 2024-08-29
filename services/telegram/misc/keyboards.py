from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from services.telegram.misc.callbacks import HomeCallback, CitySelect, \
    AdminCallback
from aiogram.utils.i18n import gettext as _


class Keyboards:
    @staticmethod
    def send_phone():
        return ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True,
                                   keyboard=[[
                                       KeyboardButton(
                                           text=_('Поделиться номером телефона'),
                                           request_contact=True)
                                   ]])

    @staticmethod
    def home() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=_("Инструкция"),
                                     callback_data=HomeCallback(
                                         action="instruction").pack()),
            ]
        ])

    @staticmethod
    def back_to_home() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        builder.button(text=_("Назад ◀️"),
                       callback_data=HomeCallback(action="back_to_home"))
        return builder.as_markup()

    @staticmethod
    def links(links: list):
        builder = InlineKeyboardBuilder()
        for i, link in enumerate(links, start=1):
            builder.button(text=_(f"Материал {i} 📎"), url=link)
        builder.adjust(1, repeat=True)
        return builder.as_markup()

    @staticmethod
    def cities(cities: list):
        builder = InlineKeyboardBuilder()
        for i, city in enumerate(cities):
            if i < 5:
                builder.button(text=f"{city}",
                               callback_data=CitySelect(name=city))
        builder.adjust(1, repeat=True)
        return builder.as_markup()

    @staticmethod
    def empty():
        return InlineKeyboardMarkup(inline_keyboard=[])

    @staticmethod
    def guest(user_id):
        builder = InlineKeyboardBuilder()
        builder.button(
            text=_("Принять ✅"),
            callback_data=AdminCallback(action="accept", user_id=user_id))
        builder.button(
            text=_("Отклонить ❌"),
            callback_data=AdminCallback(action="cancel", user_id=user_id))
        return builder.as_markup()
