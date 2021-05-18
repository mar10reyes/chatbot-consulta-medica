package com.codepalace.chatbot.utils

import com.codepalace.chatbot.utils.Constants.OPEN_GOOGLE
import com.codepalace.chatbot.utils.Constants.OPEN_SEARCH
import java.sql.Date
import java.sql.Timestamp
import java.text.SimpleDateFormat

object BotResponse {

    fun basicResponses(_message: String): String {

        val random = (0..2).random()
        val message =_message.toLowerCase()

        return when {

            //Flips a coin
            message.contains("lanza") && message.contains("una moneda") -> {
                val r = (0..1).random()
                val result = if (r == 0) "Cara" else "Sello"

                "Yo lancé una moneda y cayó $result"
            }

            //Math calculations
            message.contains("resolver") -> {
                val equation: String? = message.substringAfterLast("resolver")
                return try {
                    val answer = SolveMath.solveMath(equation ?: "0")
                    "$answer"

                } catch (e: Exception) {
                    "Disculpa, yo no puedo resolver eso"
                }
            }

            message.contains("hola") -> {
                when (random) {
                    0 -> "Hola, ¿Que sientes?"
                    1 -> "Buenas, ¿Que sintomas tiene?"
                    else -> "error" }
            }

            //Sintomas
            message.contains("tos") -> {
                when (random) {
                    0 -> "Usted posiblemente tenga gripa, debe tomar un Descongestivo "
                    else -> "error"
                }
            }
            message.contains("dolor de garganta") || message.contains("dificultad para tragar") -> {
                when (random) {
                    0 -> "Usted posiblemente tenga amigdalitis, debe tomar un Ibuprofeno "
                    else -> "error"
                }
            }
            message.contains("dolor de estomago") || message.contains("nauseas") -> {
                when (random) {
                    0 -> "Usted posiblemente tenga gastristis, debe tomar milanta"
                    else -> "error"
                }
            }

            //Fecha
            message.contains("fecha")-> {
                val timeStamp = Timestamp(System.currentTimeMillis())
                val sdf = SimpleDateFormat("dd/MM/yyyy HH:mm")
                val date = sdf.format(Date(timeStamp.time))

                date.toString()
            }

            //Open Google
            message.contains("abrir") && message.contains("google")-> {
                OPEN_GOOGLE
            }

            //Search on the internet
            message.contains("buscar")-> {
                OPEN_SEARCH
            }

            //When the programme doesn't understand...
            else -> {
                when (random) {
                    0 -> "Yo no te entiendo..."
                    1 -> "Intenta decirme otra cosa"
                    2 -> "Disculpa, ¡¿Qué?!"
                    else -> "error"
                }
            }
        }
    }
}