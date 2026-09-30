# SI3003 — INTELIGENCIA ARTIFICIAL

## Master Cheatsheet · EAFIT

---

# 0. MAPA MENTAL DEL CURSO

La idea que conecta prácticamente todo el curso es:

**Agente → percibe un estado → debe decidir qué hacer → quiere maximizar una medida de desempeño.**

Lo que cambia entre temas es **qué sabe el agente** y **qué tipo de problema intenta resolver**.

| Problema               | ¿Qué busca?                            | ¿Conoce el mundo?          | Herramienta           |
| ---------------------- | -------------------------------------- | -------------------------- | --------------------- |
| Agente racional        | Mejor acción                           | depende                    | Política              |
| Búsqueda               | Camino al objetivo                     | Sí                         | DFS, BFS, UCS, A*     |
| Optimización           | Mejor configuración                    | Sí                         | Hill Climbing, SA, GA |
| MDP                    | Mejor política bajo incertidumbre      | Sí: \(P,R\)                | Bellman, VI, PI       |
| Reinforcement Learning | Aprender política mediante experiencia | No necesariamente          | Q-Learning            |
| Supervisado            | Predecir \(y\) desde \(x\)             | Tiene ejemplos etiquetados | Árboles, regresión    |

Idea fundamental:

> **Búsqueda:** importa cómo llegamos al estado.
> **Optimización:** solo importa qué tan bueno es el estado final.
> **MDP/RL:** no escogemos un estado final; escogemos acciones repetidamente.
> **ML supervisado:** aprendemos una función desde ejemplos.

---

# 1. ¿QUÉ ES IA?

Una definición operacional clásica es el **Test de Turing**: una máquina exhibe comportamiento inteligente si un interlocutor humano no logra distinguirla de un humano mediante conversación.

Pasar un Turing Test completo implica capacidades como:

* procesamiento de lenguaje natural;
* representación del conocimiento;
* razonamiento automático;
* aprendizaje automático;
* visión;
* robótica.

La perspectiva moderna del curso se centra menos en “pensar como un humano” y más en:

## Agentes racionales

Un sistema inteligente debe escoger acciones que produzcan buenos resultados dadas:

* la información disponible;
* el entorno;
* sus objetivos;
* la incertidumbre existente.

---

# 2. AGENTES RACIONALES

## Agente

Un agente:

**percibe** el entorno mediante **sensores**
↓
procesa información
↓
ejecuta **acciones** mediante **actuadores**.

Formalmente, su comportamiento puede representarse mediante una política:

$$
\pi:\mathcal P^*\rightarrow\mathcal A
$$

donde:

* \(\mathcal P^*\): historia/secuencia de percepts;
* \(\mathcal A\): acciones posibles;
* \(\pi\): regla que escoge una acción.

---

## Racionalidad

Un agente es racional si selecciona la acción que:

$$
\boxed{\text{maximiza el valor esperado de su medida de desempeño}}
$$

dada la información disponible hasta ese momento.

**MUY IMPORTANTE:**

Racionalidad ≠ resultado perfecto.

Una buena decisión puede producir un mal resultado debido al azar.

Por tanto:

$$
\text{buena decisión}\neq\text{buen outcome necesariamente}
$$

La racionalidad evalúa la decisión **ex ante**, usando la información disponible.

---

# 3. PEAS

PEAS describe el **Task Environment**.

### P — Performance measure

¿Qué significa hacerlo bien?

### E — Environment

¿Dónde opera el agente?

### A — Actuators

¿Cómo puede actuar?

### S — Sensors

¿Qué puede observar?

Ejemplo: ajedrez

* **P:** ganar > empatar > perder.
* **E:** tablero + oponente.
* **A:** movimientos legales.
* **S:** posición actual + movimientos del rival.

---

# 4. TIPOS DE ENTORNO

## Totalmente observable vs. parcialmente observable

**Totalmente observable:** sensores muestran todo el estado relevante.

**Parcialmente observable:** existe información oculta.

Ejemplo:

* ajedrez → observable;
* póker → parcialmente observable.

---

## Determinístico vs. estocástico

### Determinístico

$$
(s,a)\rightarrow s'
$$

La acción determina completamente el siguiente estado.

### Estocástico

$$
P(s'|s,a)
$$

Una misma acción puede producir diferentes resultados.

---

## Episódico vs. secuencial

### Episódico

Cada decisión es independiente.

### Secuencial

Las acciones actuales afectan decisiones futuras.

---

## Estático vs. dinámico

### Estático

El mundo no cambia mientras el agente decide.

### Dinámico

Puede cambiar durante la deliberación.

---

## Discreto vs. continuo

Variables como:

* estados;
* tiempo;
* percepts;
* acciones

pueden ser discretas o continuas.

---

## Single-agent vs. multi-agent

¿Existe otro agente cuyo comportamiento afecta nuestras decisiones?

---

## Conocido vs. desconocido

Esto se refiere a si conocemos **cómo funciona el entorno**, no a si podemos observarlo completamente.

Esta diferencia es importante:

> **Observable:** conozco el estado actual.
> **Conocido:** conozco las reglas de transición del mundo.

---

# 5. PROGRAMAS DE AGENTE

Una política puede implementarse mediante:

* tablas;
* reglas;
* búsqueda;
* planificación;
* algoritmos de aprendizaje.

Una tabla directa:

$$
\text{historia de percepts}\rightarrow\text{acción}
$$

es conceptualmente válida pero crece exponencialmente.

Si existen \(|P|\) percepts posibles y horizonte \(T\):

$$
\sum_{t=1}^{T}|P|^t
$$

Por esto necesitamos representaciones y algoritmos más inteligentes.

---

# 6. PROBLEMAS DE BÚSQUEDA

Ahora suponemos normalmente un entorno:

* single-agent;
* observable;
* determinístico;
* conocido.

Queremos encontrar una **secuencia de acciones**.

---

## Componentes del problema

Un problema de búsqueda necesita:

$$
\boxed{S,\ s_0,\ A(s),\ Result(s,a),\ GoalTest(s),\ Cost}
$$

### Estado inicial

$$
s_0
$$

### Acciones posibles

$$
A(s)
$$

### Modelo de transición

$$
Result(s,a)=s'
$$

### Goal Test

$$
GoalTest(s)\in\{True,False\}
$$

### Costo

$$
g(n)=\text{costo acumulado desde el inicio hasta }n
$$

---

# 7. STATE SPACE VS SEARCH TREE

## State Space

Representa los estados posibles reales.

## Search Tree

Representa **secuencias de acciones exploradas**.

Dos nodos del árbol pueden representar el mismo estado si llegaron mediante caminos diferentes.

Por eso búsqueda en árbol puede repetir muchísimo trabajo.

---

# 8. FRONTIER

La **frontera** contiene los nodos generados pero todavía no expandidos.

La gran diferencia entre algoritmos de búsqueda es:

> **¿qué nodo sacamos primero de la frontera?**

---

# 9. NOTACIÓN DE COMPLEJIDAD

Usada durante búsqueda:

* \(b\): branching factor.
* \(d\): profundidad de la solución más superficial.
* \(m\): máxima profundidad del árbol.
* \(C^*\): costo de la solución óptima.
* \(\epsilon\): costo mínimo de una acción.

---

# 10. DFS — DEPTH-FIRST SEARCH

## Idea

Expandir primero el nodo **más profundo**.

## Data structure

$$
\boxed{\text{Stack — LIFO}}
$$

Last In, First Out.

---

## Propiedades

### Completo

Generalmente **NO**, si:

* existen ciclos;
* la profundidad puede ser infinita.

Puede ser completo en espacios finitos evitando ciclos.

### Óptimo

$$
\boxed{\text{NO}}
$$

Encuentra una solución profunda sin necesariamente encontrar la mejor.

### Tiempo

$$
O(b^m)
$$

### Memoria

Mucho menor que BFS.

Aproximadamente:

$$
O(bm)
$$

### Úsalo cuando

* memoria es crítica;
* soluciones pueden estar profundas;
* optimalidad no importa.

---

# 11. BFS — BREADTH-FIRST SEARCH

## Idea

Expandir primero el nodo **menos profundo**.

## Data structure

$$
\boxed{\text{Queue — FIFO}}
$$

First In, First Out.

---

## Completo

Sí si:

$$
b<\infty,\quad d<\infty
$$

---

## Óptimo

Solo cuando el costo aumenta con la profundidad.

Caso clásico:

$$
c(a)=1
$$

para todas las acciones.

Entonces encontrar el camino con menos acciones = menor costo.

---

## Tiempo

$$
O(b^d)
$$

o según la convención exacta del árbol:

$$
O(b^{d+1})
$$

---

## Memoria

$$
O(b^d)
$$

El gran problema de BFS es **memoria**.

---

# 12. UCS — UNIFORM COST SEARCH

Escoge el nodo con:

$$
\boxed{\min g(n)}
$$

donde \(g(n)\) es el costo acumulado.

## Data structure

**Priority queue**

prioridad:

$$
g(n)
$$

---

## Completo

Sí, si:

$$
c(s,a,s')\geq\epsilon>0
$$

---

## Óptimo

$$
\boxed{\text{SÍ}}
$$

---

## Complejidad

Profundidad efectiva:

$$
\frac{C^*}{\epsilon}
$$

Tiempo y espacio:

$$
O\left(b^{C^*/\epsilon}\right)
$$

---

# 13. BFS VS UCS

Si todos los costos son iguales:

$$
\boxed{BFS\approx UCS}
$$

porque minimizar número de pasos también minimiza costo.

Pero si los costos varían:

**BFS**

$$
\min depth
$$

**UCS**

$$
\min cost
$$

---

# 14. HEURÍSTICAS

Una heurística:

$$
h(n)
$$

estima el costo restante desde \(n\) hasta una solución.

Ejemplo GPS:

$$
h(n)=\text{distancia en línea recta al destino}
$$

No representa necesariamente el costo verdadero.

---

# 15. GREEDY BEST-FIRST SEARCH

Escoge:

$$
\boxed{\min h(n)}
$$

Solo pregunta:

> “¿Qué parece estar más cerca del objetivo?”

Ignora completamente:

$$
g(n)
$$

---

## Propiedades

* Completo: no necesariamente.
* Óptimo: no.
* Tiempo peor caso:

$$
O(b^m)
$$

* Espacio:

$$
O(b^m)
$$

Su rendimiento depende muchísimo de la heurística.

---

# 16. A*

Combina:

$$
\boxed{f(n)=g(n)+h(n)}
$$

donde:

* \(g(n)\): costo que ya pagué;
* \(h(n)\): costo esperado que falta.

Interpretación:

$$
f(n)=\text{estimación del costo total de una solución vía }n
$$

---

# 17. HEURÍSTICA ADMISIBLE

Una heurística es admisible si **nunca sobreestima** el costo verdadero.

$$
\boxed{0\leq h(n)\leq h^*(n)}
$$

donde \(h^*(n)\) es el verdadero costo óptimo restante.

Además:

$$
h(goal)=0
$$

Con una heurística admisible, A* Tree Search puede encontrar una solución óptima.

---

# 18. HEURÍSTICA CONSISTENTE

También llamada monotónica.

Debe cumplir:

$$
\boxed{h(n)\leq c(n,a,n')+h(n')}
$$

Es esencialmente una desigualdad triangular.

Interpretación:

> Estimar ir al objetivo directamente nunca debería ser más caro que ir primero a un vecino y luego estimar desde ahí.

Consecuencia:

$$
f(n)=g(n)+h(n)
$$

no disminuye a medida que avanzamos por un camino.

**Consistente ⇒ admisible.**

---

# 19. COMPARACIÓN BÚSQUEDA

| Método |          Prioridad | Completo |         Óptimo |
| ------ | -----------------: | -------: | -------------: |
| DFS    |        profundidad |      No* |             No |
| BFS    | profundidad mínima |       Sí | costos iguales |
| UCS    |           \(g(n)\) |       Sí |             Sí |
| Greedy |           \(h(n)\) |      No* |             No |
| A*     |            \(g+h\) |     Sí** |           Sí** |

* dependiendo del manejo de ciclos.
** bajo condiciones apropiadas de la heurística/costos.

---

# 20. SEARCH VS OPTIMIZATION

Hasta ahora:

$$
s_0\rightarrow s_1\rightarrow s_2\rightarrow goal
$$

El **camino importa**.

En optimización:

$$
\boxed{\text{solo importa la calidad de la configuración final}}
$$

---

# 21. PROBLEMA DE OPTIMIZACIÓN

Tiene:

### Estados candidatos

Configuraciones completas.

### Función objetivo

$$
value(s)
$$

Queremos:

$$
\max_s value(s)
$$

o equivalentemente:

$$
\min_s cost(s)
$$

### Vecindario

Estados alcanzables mediante pequeños cambios en \(s\).

---

# 22. LOCAL SEARCH

Mantiene únicamente:

* un estado;
* o un pequeño conjunto de estados.

No mantiene el árbol completo.

### Ventaja

$$
\boxed{\text{memoria extremadamente baja}}
$$

Puede operar incluso en espacios gigantes o continuos.

### Desventaja

Generalmente pierde garantías de:

* completitud;
* optimalidad.

---

# 23. HILL CLIMBING

Idea:

1. comienza en un estado;
2. analiza vecinos;
3. escoge uno mejor;
4. repite;
5. para cuando ninguno mejora.

Es una estrategia **greedy local**.

---

## Ejemplo: 8 Queens

Estado:

8 reinas, una por columna.

Costo:

$$
h(s)=\#\text{ pares de reinas que se atacan}
$$

Objetivo:

$$
\boxed{h(s)=0}
$$

Vecino:

mover una reina dentro de su columna.

---

# 24. PROBLEMAS DE HILL CLIMBING

## Local optimum

Un estado mejor que todos sus vecinos pero peor que otro estado lejano.

---

## Plateau

Región donde:

$$
value(s)=value(neighbor)
$$

No existe dirección evidente.

---

## Ridge

El óptimo requiere una combinación de movimientos que individualmente no parecen mejorar.

---

# 25. VARIANTES DE HILL CLIMBING

### Steepest-Ascent

Evalúa todos los vecinos y elige el mejor.

### First-Choice

Prueba vecinos aleatoriamente hasta encontrar uno mejor.

### Sideways Moves

Permite movimientos con:

$$
\Delta value=0
$$

para atravesar plateaus.

### Random Restart

Ejecuta hill climbing desde múltiples estados iniciales.

### Stochastic Hill Climbing

Escoge aleatoriamente entre movimientos que mejoran.

---

# 26. GRADIENT DESCENT

Hill climbing en espacios continuos conduce naturalmente a:

$$
\boxed{\text{gradient ascent/descent}}
$$

Para minimizar:

$$
\theta_{t+1}
=
\theta_t-\alpha\nabla f(\theta_t)
$$

donde:

* \(\nabla f\): dirección de máximo incremento;
* \(-\nabla f\): dirección de máximo descenso;
* \(\alpha\): learning rate.

Este concepto conecta optimización clásica con machine learning.

---

# 27. SIMULATED ANNEALING

Solución al problema de quedar atrapado en óptimos locales.

Acepta:

* movimientos mejores → siempre;
* movimientos peores → algunas veces.

Si:

$$
\Delta E=value(next)-value(current)
$$

y:

$$
\Delta E<0
$$

se acepta con probabilidad:

$$
\boxed{
P(\text{accept})=
e^{\Delta E/T}
}
$$

---

# 28. TEMPERATURA \(T\)

### \(T\) alta

Muchos movimientos malos son aceptados.

$$
\rightarrow\text{exploración}
$$

### \(T\) baja

Movimientos malos casi nunca se aceptan.

$$
\rightarrow\text{explotación}
$$

### \(T\to0\)

Simulated Annealing se comporta aproximadamente como hill climbing.

Con un cooling schedule suficientemente lento existe convergencia teórica hacia el óptimo global con probabilidad tendiente a 1, aunque en implementaciones finitas no existe garantía práctica de optimalidad.

---

# 29. LOCAL BEAM SEARCH

En vez de mantener un único estado:

$$
\boxed{k\text{ estados}}
$$

1. expandir los \(k\);
2. combinar sucesores;
3. seleccionar los \(k\) mejores;
4. repetir.

Problema:

todos pueden terminar concentrándose en la misma región.

### Stochastic Beam Search

Selecciona estados proporcionalmente a su fitness en lugar de quedarse siempre con los mejores.

---

# 30. GENETIC ALGORITHMS

Mantienen una **población** de soluciones.

Una solución:

$$
x=(x_1,\ldots,x_L)
$$

se interpreta como un cromosoma.

Proceso:

$$
\boxed{
Selection\rightarrow Crossover\rightarrow Mutation\rightarrow New\ Generation
}
$$

---

## Fitness

Mide la calidad de una solución.

Ejemplo 8-reinas:

máximo número de pares:

$$
{8\choose2}=28
$$

Por tanto:

$$
\boxed{
fitness(x)=28-n_{\text{conflictos}}
}
$$

---

# 31. PROGRAMACIÓN LINEAL

Problema:

$$
\boxed{\max c^Tx}
$$

sujeto a:

$$
Ax\leq b
$$

y normalmente:

$$
x\geq0
$$

Todo debe ser **lineal**:

* función objetivo;
* restricciones.

---

## LP

Variables continuas.

Puede resolverse eficientemente y de forma exacta.

## ILP

Variables enteras.

$$
x_i\in\mathbb Z
$$

Esto vuelve el problema considerablemente más difícil.

Aplicaciones:

* producción;
* logística;
* portafolios;
* planificación;
* asignación de recursos.

---

# 32. MDP — MARKOV DECISION PROCESS

Ahora ocurren tres cambios:

1. decisiones son secuenciales;
2. resultados son estocásticos;
3. queremos una política completa.

Un MDP se representa mediante:

$$
\boxed{(S,A,P,R,\gamma)}
$$

---

## \(S\)

Estados.

## \(A\)

Acciones.

## \(P\)

Modelo de transición:

$$
P(s'|s,a)
$$

## \(R\)

Reward.

## \(\gamma\)

Discount factor.

$$
0\leq\gamma\leq1
$$

---

# 33. MARKOV PROPERTY

$$
\boxed{
P(s_{t+1}|s_t,a_t,s_{t-1},\ldots)
=
P(s_{t+1}|s_t,a_t)
}
$$

Interpretación:

> El estado actual contiene toda la información relevante del pasado para predecir el futuro.

---

# 34. PLAN VS POLICY

### Search

Encuentra un plan:

$$
[a_1,a_2,a_3,\ldots]
$$

### MDP

Encuentra:

$$
\boxed{\pi:S\rightarrow A}
$$

porque no conocemos de antemano exactamente qué estado resultará de nuestras acciones.

---

# 35. REWARD VS VALUE

Esta diferencia es FUNDAMENTAL.

## Reward

$$
R(s)
$$

Beneficio inmediato.

## Value

$$
V(s)
$$

Beneficio total esperado desde ese estado hacia el futuro.

Así:

$$
\boxed{\text{reward = corto plazo}}
$$

$$
\boxed{\text{value = largo plazo}}
$$

---

# 36. DISCOUNTING

Retorno:

$$
\boxed{
G_0=\sum_{t=0}^{\infty}\gamma^tR(s_t)
}
$$

Ejemplo:

$$
G_0=
R_0+\gamma R_1+\gamma^2R_2+\cdots
$$

---

## Interpretación de \(\gamma\)

### \(\gamma\approx0\)

Agente miope.

Le importa principalmente recompensa inmediata.

### \(\gamma\approx1\)

Agente de largo plazo.

Las recompensas futuras siguen siendo relevantes.

Horizonte efectivo aproximadamente relacionado con:

$$
\frac{1}{1-\gamma}
$$

---

# 37. ¿POR QUÉ DESCONTAR?

Tres razones:

### Preferencia temporal

Recompensa hoy > recompensa lejana.

### Convergencia matemática

Si:

$$
0<\gamma<1
$$

y:

$$
|R_t|\leq R_{max}
$$

entonces:

$$
\sum_{t=0}^{\infty}\gamma^tR_t
\leq
\frac{R_{max}}{1-\gamma}
$$

### Incertidumbre

Eventos muy lejanos son menos seguros.

---

# 38. VALUE FUNCTION

Para una política \(\pi\):

$$
\boxed{
V^\pi(s)=
E_\pi
\left[
\sum_{t=0}^{\infty}\gamma^tR(s_t)
\mid s_0=s
\right]
}
$$

Pregunta:

> “Si empiezo en \(s\) y sigo \(\pi\), ¿cuánto espero ganar?”

---

# 39. BELLMAN EQUATION

En vez de sumar infinitas recompensas:

$$
\boxed{
V^\pi(s)
=
R(s)
+
\gamma
\sum_{s'}
P(s'|s,\pi(s))V^\pi(s')
}
$$

Interpretación:

$$
\boxed{\text{valor actual}
=
\text{reward inmediato}
+
\text{valor esperado del futuro}}
$$

La ecuación de Bellman **no es una aproximación**. Es una reescritura recursiva de la definición de valor.

---

# 40. BELLMAN OPTIMALITY EQUATION

Si queremos la mejor política:

$$
\boxed{
V^*(s)
=
R(s)
+
\gamma
\max_a
\sum_{s'}
P(s'|s,a)V^*(s')
}
$$

---

# 41. Q-VALUE

Definimos:

$$
\boxed{
Q(s,a)
=
R(s)
+
\gamma
\sum_{s'}
P(s'|s,a)V(s')
}
$$

Interpretación:

> Valor esperado si estoy en \(s\), ejecuto \(a\), y después actúo óptimamente.

---

# 42. EXTRAER POLÍTICA

Una vez conocemos \(V^*\):

$$
\boxed{
\pi^*(s)
=
\arg\max_a
\sum_{s'}
P(s'|s,a)V^*(s')
}
$$

`max` → da el valor.

`argmax` → da la acción que produce ese valor.

---

# 43. VALUE ITERATION

Inicializar:

$$
V_0(s)=0
$$

Actualizar:

$$
\boxed{
V_{k+1}(s)
=
R(s)+
\gamma\max_a
\sum_{s'}
P(s'|s,a)V_k(s')
}
$$

Repetir hasta:

$$
\max_s|V_{k+1}(s)-V_k(s)|<\theta
$$

---

## Convergencia

Para \(\gamma<1\), Bellman es una contracción:

$$
\boxed{
\|V_{k+1}-V'_{k+1}\|_\infty
\leq
\gamma
\|V_k-V'_k\|_\infty
}
$$

Por tanto converge a una solución única.

---

# 44. POLICY ITERATION

Alterna:

## 1. Policy Evaluation

Fijar \(\pi\) y resolver:

$$
V^\pi(s)
=
R(s)+
\gamma
\sum_{s'}
P(s'|s,\pi(s))V^\pi(s')
$$

Es un sistema lineal.

## 2. Policy Improvement

$$
\pi'(s)
=
\arg\max_a
\sum_{s'}
P(s'|s,a)V^\pi(s')
$$

Repetir hasta:

$$
\pi'=\pi
$$

---

# 45. VALUE ITERATION VS POLICY ITERATION

|                   | Value Iteration   | Policy Iteration           |
| ----------------- | ----------------- | -------------------------- |
| Actualiza         | \(V\)             | \(\pi\) y \(V^\pi\)        |
| Iteración         | barata            | cara                       |
| Convergencia      | asintótica        | política exacta finita     |
| Espacios grandes  | normalmente mejor | sistema lineal costoso     |
| Espacios pequeños | bueno             | puede converger muy rápido |

En el Gridworld usado en el material:

* VI: ~30 barridos;
* PI: ~5 iteraciones.

---

# 46. MDP VS REINFORCEMENT LEARNING

Esta distinción es una de las más importantes del curso.

## MDP / planificación

Conocemos:

$$
P(s'|s,a)
$$

y:

$$
R(s)
$$

Podemos resolver matemáticamente el problema.

## RL

No necesariamente conocemos \(P\) ni \(R\).

El agente debe:

$$
\boxed{\text{actuar}\rightarrow\text{observar}\rightarrow\text{aprender}}
$$

---

# 47. REINFORCEMENT LEARNING

En RL el agente aprende mediante:

$$
\boxed{\text{trial and error + rewards}}
$$

No recibe la acción correcta explícitamente.

Objetivo:

$$
\boxed{\pi^*}
$$

que maximiza recompensa acumulada esperada.

---

# 48. VALUE-BASED VS POLICY-BASED RL

## Policy-Based

Aprender directamente:

$$
\boxed{\pi_\theta(a|s)}
$$

Estado → acción/distribución.

---

## Value-Based

Aprender:

$$
V(s)
$$

o:

$$
Q(s,a)
$$

Después obtener política de manera greedy.

$$
\boxed{
\pi(s)=\arg\max_aQ(s,a)
}
$$

---

# 49. STATE VALUE VS ACTION VALUE

## State Value

$$
V^\pi(s)
$$

Retorno esperado empezando en \(s\).

## Action Value

$$
Q^\pi(s,a)
$$

Retorno esperado:

1. empezando en \(s\);
2. tomando \(a\);
3. siguiendo luego \(\pi\).

---

# 50. Q-LEARNING

Q-Learning aprende:

$$
\boxed{Q^*(s,a)}
$$

sin conocer explícitamente las probabilidades de transición.

Es:

* value-based;
* temporal-difference;
* off-policy.

---

# 51. Q TABLE

Para estados discretos:

| State   |    Up |  Down |  Left | Right |
| ------- | ----: | ----: | ----: | ----: |
| \(s_1\) | \(Q\) | \(Q\) | \(Q\) | \(Q\) |
| \(s_2\) | \(Q\) | \(Q\) | \(Q\) | \(Q\) |

Inicialmente:

$$
Q(s,a)=0
$$

Durante el entrenamiento los valores mejoran.

---

# 52. Q-LEARNING UPDATE

La actualización fundamental:

$$
\boxed{
Q(s,a)
\leftarrow
Q(s,a)
+
\alpha
\left[
r+
\gamma
\max_{a'}Q(s',a')
-
Q(s,a)
\right]
}
$$

Partes:

### Current estimate

$$
Q(s,a)
$$

### Target

$$
r+\gamma\max_{a'}Q(s',a')
$$

### TD Error

$$
\boxed{
\delta=
r+\gamma\max_{a'}Q(s',a')
-Q(s,a)
}
$$

Por tanto:

$$
Q\leftarrow Q+\alpha\delta
$$

---

# 53. LEARNING RATE

$$
\alpha\in[0,1]
$$

### \(\alpha\approx0\)

Aprendizaje lento.

Mantiene conocimiento anterior.

### \(\alpha\approx1\)

Actualización muy agresiva.

Le da muchísimo peso a observación reciente.

---

# 54. EXPLORATION VS EXPLOITATION

## Exploration

Probar acciones desconocidas.

> “Quizás exista algo mejor.”

## Exploitation

Usar lo que actualmente creemos que es mejor.

> “Uso la mejor opción conocida.”

Necesitamos ambos.

---

# 55. EPSILON-GREEDY

Con probabilidad:

$$
\epsilon
$$

escoger acción aleatoria.

Con probabilidad:

$$
1-\epsilon
$$

escoger:

$$
\arg\max_aQ(s,a)
$$

Normalmente:

$$
\epsilon_{initial}\text{ alto}
$$

y después:

$$
\epsilon\downarrow
$$

Así:

inicio → exploración
final → explotación.

---

# 56. ¿POR QUÉ Q-LEARNING ES OFF-POLICY?

La acción observada puede venir de una política exploratoria:

$$
\epsilon\text{-greedy}
$$

pero el target usa:

$$
\boxed{\max_{a'}Q(s',a')}
$$

es decir, evalúa la acción greedy futura.

Por tanto:

**behavior policy ≠ target policy**

→ off-policy.

---

# 57. SUPERVISED LEARNING

Ahora sí tenemos ejemplos:

$$
\boxed{
D=\{(x_i,y_i)\}_{i=1}^{N}
}
$$

Queremos aprender:

$$
h(x)\approx y
$$

que generalice a observaciones nuevas.

---

# 58. TIPOS DE APRENDIZAJE

## Supervisado

Tenemos respuestas correctas:

$$
(x,y)
$$

## Reinforcement Learning

Tenemos rewards pero no la respuesta correcta para cada decisión.

## No supervisado

Tenemos únicamente:

$$
x
$$

sin labels.

---

# 59. CLASSIFICATION VS REGRESSION

## Classification

$$
y\in\{c_1,\ldots,c_k\}
$$

Ejemplos:

* spam/no spam;
* fraude/no fraude;
* dígito 0–9.

## Regression

$$
y\in\mathbb R
$$

Ejemplo:

* precio;
* temperatura;
* ingreso.

---

# 60. FEATURES

Una entrada debe convertirse en atributos:

$$
\boxed{x=(x_1,x_2,\ldots,x_d)}
$$

Ejemplo spam:

* presencia de “FREE”;
* cantidad de `!`;
* mayúsculas;
* remitente;
* links sospechosos.

Ejemplo imagen:

* pixels;
* bordes;
* formas;
* representaciones aprendidas.

---

# 61. HIPÓTESIS

Un modelo aprendido es una hipótesis:

$$
h\in H
$$

donde \(H\) es el **hypothesis space**.

Machine learning implica responder:

1. ¿qué \(H\) usamos?
2. ¿qué hipótesis ajusta mejor?
3. ¿cómo equilibramos fit y complejidad?

---

# 62. OCCAM'S RAZOR

Entre dos hipótesis que explican los datos:

> Preferir generalmente la más simple.

¿Por qué?

Una hipótesis extremadamente compleja puede memorizar el training set sin generalizar.

---

# 63. DECISION TREES

Un árbol consiste en:

### Internal nodes

Tests sobre atributos.

### Branches

Resultados posibles.

### Leaves

Predicción final.

Ejemplo:

```text
          Patrons?
         /    |    \
      None   Some   Full
       No     Yes     ...
```

---

# 64. EXPRESSIVITY OF DECISION TREES

Un árbol discreto puede representar **cualquier función discreta**.

Problema:

también puede memorizar todo el dataset.

Un árbol enorme puede tener:

$$
\text{training accuracy}=100\%
$$

pero generalizar mal.

Por eso buscamos árboles **compactos**.

---

# 65. DECISION TREE LEARNING

Proceso recursivo:

1. Si todos tienen la misma clase → hoja.
2. Si no quedan atributos → clase mayoritaria.
3. Elegir el mejor atributo.
4. Dividir dataset.
5. Repetir para cada rama.

El atributo elegido maximiza:

$$
\boxed{Importance(A)}
$$

En este curso se usa **Information Gain**.

---

# 66. ENTROPÍA

Mide incertidumbre.

Para \(K\) clases:

$$
\boxed{
H(Y)
=
-\sum_{k=1}^{K}
p_k\log_2p_k
}
$$

---

## Caso binario

$$
\boxed{
H(p)
=
-p\log_2p
-
(1-p)\log_2(1-p)
}
$$

---

## Casos que debes reconocer

### Totalmente puro

$$
(1,0)
$$

$$
H=0
$$

### Máxima incertidumbre binaria

$$
(0.5,0.5)
$$

$$
H=1
$$

### 90/10

$$
H\approx0.47
$$

---

# 67. INFORMATION GAIN

Antes:

$$
H(E)
$$

Después de dividir según \(A\):

$$
\boxed{
H(E|A)
=
\sum_k
\frac{|E_k|}{|E|}
H(E_k)
}
$$

Entonces:

$$
\boxed{
Gain(A)=H(E)-H(E|A)
}
$$

---

## Interpretación

### Gain alto

El atributo reduce mucho la incertidumbre.

### Gain bajo

No ayuda demasiado.

### Gain = 0

No proporciona información sobre la etiqueta.

---

# 68. TRAIN / VALIDATION / TEST

## Training set

Aprender parámetros/modelo.

## Validation set

Escoger:

* hiperparámetros;
* arquitectura;
* complejidad;
* mejor modelo.

## Test set

Evaluación FINAL.

Regla:

$$
\boxed{\text{Never peek at the test set}}
$$

Si escogemos el modelo mirando test:

$$
\text{test}\rightarrow\text{validation disfrazado}
$$

y la estimación deja de ser verdaderamente out-of-sample.

---

# 69. ACCURACY

Para clasificación:

$$
\boxed{
Accuracy=
\frac{\#\ correctas}{\#\ total}
}
$$

---

# 70. LEARNING CURVE

Graficar:

$$
\text{performance}
$$

contra:

$$
\text{training set size}
$$

Sirve para entender cuánto mejora el modelo al obtener más datos.

---

# 71. LINEAR REGRESSION

Modelo:

$$
\boxed{
h_w(x)=w_0+w_1x
}
$$

donde:

* \(w_0\): intercept;
* \(w_1\): pendiente.

---

# 72. RESIDUAL

$$
\boxed{
e_i=y_i-\hat y_i
}
$$

Es la diferencia entre observado y predicho.

---

# 73. L2 / SUM OF SQUARED ERRORS

$$
\boxed{
L(w_0,w_1)
=
\sum_j
\left[y_j-(w_0+w_1x_j)\right]^2
}
$$

Objetivo:

$$
\boxed{
w^*=
\arg\min_w L(w)
}
$$

En el óptimo:

$$
\frac{\partial L}{\partial w_0}=0
$$

$$
\frac{\partial L}{\partial w_1}=0
$$

Esto permite obtener una solución analítica para regresión lineal simple.

---

# 74. LAS DISTINCIONES QUE MÁS SE CONFUNDEN

### Reward vs Value

$$
R(s)=\text{beneficio inmediato}
$$

$$
V(s)=\text{beneficio futuro acumulado esperado}
$$

---

### \(V(s)\) vs \(Q(s,a)\)

$$
V(s)=\text{qué tan bueno es estar en }s
$$

$$
Q(s,a)=\text{qué tan bueno es hacer }a\text{ desde }s
$$

---

### \(g(n)\) vs \(h(n)\) vs \(f(n)\)

$$
g(n)=\text{costo ya pagado}
$$

$$
h(n)=\text{estimación de lo que falta}
$$

$$
f(n)=g(n)+h(n)
$$

---

### BFS vs UCS

BFS:

$$
\min depth
$$

UCS:

$$
\min g
$$

---

### Greedy vs A*

Greedy:

$$
h
$$

A*:

$$
g+h
$$

---

### Search vs Optimization

Search:

$$
\text{importa camino}
$$

Optimization:

$$
\text{importa estado final}
$$

---

### MDP vs RL

MDP planning:

$$
P,R\text{ conocidos}
$$

RL:

$$
P,R\text{ se descubren mediante interacción}
$$

---

### Supervised Learning vs RL

Supervised:

$$
\text{respuesta correcta por ejemplo}
$$

RL:

$$
\text{reward, pero no necesariamente acción correcta}
$$

---

### Classification vs Regression

Classification:

$$
y=\text{categoría}
$$

Regression:

$$
y=\text{valor continuo}
$$

---

# 75. FORMULARIO ULTRACOMPACTO

## Search

$$
g(n)=\text{cost so far}
$$

$$
h(n)=\text{estimated cost to goal}
$$

$$
f(n)=g(n)+h(n)
$$

A*:

$$
\boxed{f=g+h}
$$

Consistencia:

$$
\boxed{h(n)\leq c(n,n')+h(n')}
$$

---

## Simulated Annealing

$$
\boxed{
P(\text{accept worse})
=e^{\Delta E/T}
}
$$

---

## MDP

$$
\boxed{MDP=(S,A,P,R,\gamma)}
$$

$$
\boxed{
G_t=
\sum_{k=0}^{\infty}\gamma^kR_{t+k}
}
$$

Bellman:

$$
\boxed{
V^\pi(s)
=
R(s)
+
\gamma
\sum_{s'}
P(s'|s,\pi(s))V^\pi(s')
}
$$

Optimal Bellman:

$$
\boxed{
V^*(s)
=
R(s)+
\gamma
\max_a
\sum_{s'}
P(s'|s,a)V^*(s')
}
$$

Optimal policy:

$$
\boxed{
\pi^*(s)
=
\arg\max_a
\sum_{s'}
P(s'|s,a)V^*(s')
}
$$

---

## Q-Learning

$$
\boxed{
Q(s,a)
\leftarrow
Q(s,a)
+
\alpha
[
r+
\gamma\max_{a'}Q(s',a')
-
Q(s,a)
]
}
$$

TD error:

$$
\boxed{
\delta=
r+\gamma\max_{a'}Q(s',a')-Q(s,a)
}
$$

Policy:

$$
\boxed{
\pi(s)=\arg\max_aQ(s,a)
}
$$

---

## Decision Trees

Entropy:

$$
\boxed{
H(Y)
=
-\sum_kp_k\log_2p_k
}
$$

Conditional entropy:

$$
\boxed{
H(E|A)
=
\sum_k
\frac{|E_k|}{|E|}
H(E_k)
}
$$

Information Gain:

$$
\boxed{
Gain(A)=H(E)-H(E|A)
}
$$

---

## Linear Regression

$$
\boxed{
\hat y=w_0+w_1x
}
$$

Residual:

$$
\boxed{
e=y-\hat y
}
$$

Loss:

$$
\boxed{
L(w)=\sum_i(y_i-\hat y_i)^2
}
$$

Optimization:

$$
\boxed{
w^*=\arg\min_wL(w)
}
$$

---

# 76. ALGORITMO A ESCOGER — GUÍA DE 10 SEGUNDOS

**Necesito encontrar una ruta/camino**
→ Search.

**Todos los pasos cuestan lo mismo**
→ BFS.

**Los costos son distintos**
→ UCS.

**Tengo una estimación buena hacia el objetivo**
→ A*.

**No me importa el camino, solo encontrar una configuración buena**
→ Local Search.

**Tengo enorme espacio y acepto solución aproximada**
→ Hill Climbing / Simulated Annealing.

**Me preocupa quedar atrapado en óptimo local**
→ Simulated Annealing / Random Restart.

**Objetivo y restricciones son lineales**
→ Linear Programming.

**Debo escoger acciones repetidamente con resultados probabilísticos y conozco el modelo**
→ MDP.

**Conozco MDP y quiero \(V^*\)**
→ Value Iteration.

**MDP pequeño y quiero alternar evaluación/mejora de políticas**
→ Policy Iteration.

**No conozco cómo funciona el mundo y debo aprender mediante rewards**
→ Reinforcement Learning.

**Estados/acciones discretos y quiero aprender valores**
→ Q-Learning.

**Tengo ejemplos \(x,y\)**
→ Supervised Learning.

**\(y\) es categoría**
→ Classification.

**\(y\) es continuo**
→ Regression.

**Quiero modelo interpretable de clasificación**
→ Decision Tree.

---

# 77. EL HILO CONDUCTOR QUE DEBES ENTENDER

Todo el bloque puede condensarse en una sola progresión:

$$
\boxed{
\text{Agent}
\rightarrow
\text{Search}
\rightarrow
\text{Optimization}
\rightarrow
\text{MDP}
\rightarrow
\text{RL}
\rightarrow
\text{Machine Learning}
}
$$

Primero preguntamos:

> ¿Qué significa actuar racionalmente?

Después:

> Si conozco el mundo, ¿cómo encuentro una buena secuencia de acciones?

Luego:

> Si solo importa la solución final, ¿cómo optimizo sin recorrer todo?

Después:

> Si las acciones son inciertas, ¿cómo encuentro la mejor política?

Luego:

> Si ni siquiera conozco las reglas del mundo, ¿cómo las aprendo interactuando?

Finalmente:

> Si tengo ejemplos de respuestas correctas, ¿cómo aprendo una función que generalice?

Ese es el esquema conceptual central del material disponible actualmente en SI3003.
