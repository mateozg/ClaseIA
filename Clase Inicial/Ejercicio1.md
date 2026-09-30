# Ficha de análisis: Analizando Agentes de IA con Hugging Face Spaces

## 1. Nombre del Space

**Nombre:** LingBot-Video MoE 30B-A3B

**Enlace:** https://huggingface.co/spaces/victor/lingbot-video 

------------------------------------------------------------------------

## 2. ¿Qué hace el agente?

Puede generar videos a partir de texto, videos a partir de imagenes o generar imagenes a partir de texto. El usuario ingresa un prompt (una imagen tambien si es la opcion image -> video), puede modificar las opciones avanzadas y se obtiene lo pedido. viene vinculado con un mejorador de prompts en caso de que los textos dados sean muy cortos

------------------------------------------------------------------------

## 3. Análisis PEAS

  Elemento          Respuesta
  ----------------- ----------------------------------------------------
  **Performance**:   Que el video se parezca al prompt, tenga buena calidad y coherencia.
  
  **Environment**:   Usuario, interfaz de Hugging Face, servidor donde corre el modelo.
  
  **Actuators**:     Mejora el prompt ingresado para obtener mejores resultados, muestra una barra de progreso durante la generacion y entrega el video/la imagen terminado
  
  **Sensors**:      Recibe un prompot con la descripcion de lo que quiere el usuario en el caso de image -> video, recibe una imagen base

------------------------------------------------------------------------

## 4. Clasificación del entorno

  Propiedad      Clasificación     Justificación
  -------------- ----------------- ---------------
  Observable:    Parcial ->          Solo conoce el prompt que recibe.
  
  Determinista:   No   ->             El mismo prompt puede generar resultados diferentes.
  
  Episódico:      Sí     ->           Cada generación es independiente.
  
  Estático:       Sí       ->         El prompt no cambia mientras se genera el video/la imagen.
  
  Discreto:       No       ->         Trabaja con texto e imágenes continuas.
  
  Conocido:       Sí        ->        El modelo y las reglas de funcionamiento ya están definidas.         

------------------------------------------------------------------------

## 5. ¿Qué tipo de programa de agente creen que es?

Agente basado en objetivos.

Porque recibe un objetivo (el prompt) y trata de generar un video que cumpla con lo que pidió el usuario. El hecho de que existe un mejorador de prompts que mejor define como deberian de ser construidos los objetivos, implica que se entre mas objetivos a cumplir, mejor se obtiene el resultado final.

------------------------------------------------------------------------

# Reto adicional

1.  **Totalmente observable, determinista y episódico.**
    - Unlimited-OCR
    - https://huggingface.co/spaces/baidu/Unlimited-OCR
        - Totalmente observable: Recibe la imagen completa que debe procesar.
        - Determinista: La misma imagen produce el mismo resultado.
        - Episódico: Cada imagen se procesa de forma independiente.

2.  **Parcialmente observable, estocástico y secuencial.**
    - Gemma Avatar
    - https://huggingface.co/spaces/victor/gemma-avatar
        - Parcialmente observable: Solo conoce la información que el usuario le dice por voz; no tiene acceso a todo el contexto o intención del usuario.
        - Estocástico: Las respuestas del modelo conversacional pueden variar incluso con entradas similares, ya que utiliza un LLM generativo.
        - Secuencial: Mantiene una conversación en tiempo real. Cada respuesta depende de los mensajes anteriores.

------------------------------------------------------------------------
