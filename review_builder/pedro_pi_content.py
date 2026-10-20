"""Conteúdo pedagógico da revisão PI — Pedro, 6º ano, 2º trimestre (8 disciplinas + simulado)."""

from __future__ import annotations

REVIEW_ID = "pedro-pi-6ano"
STUDENT_NAME = "Pedro"
GRADE = "6º ano"
PAGE_TITLE = f"Revisão Multidisciplinar — {STUDENT_NAME} ({GRADE})"

PERCURSO_STEPS = """
            <ol>
              <li>Comece pelo <strong>Resumo</strong> para ver tabelas e ideias-chave.</li>
              <li>Depois leia a <strong>Explicação geral</strong> com calma.</li>
              <li>Faça os <strong>exercícios</strong> sem olhar a resposta.</li>
              <li>Use <em>Mostrar resposta/modelo</em> só depois de tentar.</li>
              <li>Leia as <strong>Dicas finais de prova</strong> antes da PI.</li>
            </ol>"""


def _mc(question: str, options: list[str], correct: int, explanation: str, model: str) -> dict:
    return {
        "type": "multiple-choice",
        "question": question,
        "options": options,
        "correctAnswer": correct,
        "explanation": explanation,
        "modelAnswer": model,
    }


def _sa(question: str, keywords: list[str], explanation: str, model: str) -> dict:
    return {
        "type": "short-answer",
        "question": question,
        "keywords": keywords,
        "explanation": explanation,
        "modelAnswer": model,
    }


def build_subjects() -> dict:
    return {
        "ingles": _subject_ingles(),
        "geografia": _subject_geografia(),
        "matematica": _subject_matematica(),
        "desenho": _subject_desenho(),
        "ciencias": _subject_ciencias(),
        "portugues": _subject_portugues(),
        "espanhol": _subject_espanhol(),
        "historia": _subject_historia(),
    }


def _subject_ingles() -> dict:
    return {
        "title": "Inglês",
        "icon": "EN",
        "sections": {
            "percurso": f"""
            <p>Conteúdo da <strong>Unit 5</strong> (Macmillan): <em>Simple Past</em> e <em>Past Progressive</em>,
            conectores <span class="hl">when</span> e <span class="hl">while</span>, formação do gerúndio (-ing).</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Past Progressive (was/were + -ing)</h3>
            <p>Descreve uma ação <strong>em andamento</strong> no passado:</p>
            <ul>
              <li><span class="hl">was</span> + -ing → I / he / she / it: <em>I was doing my homework.</em></li>
              <li><span class="hl">were</span> + -ing → you / we / they: <em>They were playing soccer.</em></li>
              <li>Negativo: <span class="hl--no">wasn't / weren't</span> + -ing</li>
              <li>Pergunta: <em>Was I…? / Were you…?</em> — resposta curta: <em>Yes, I was.</em> / <em>No, I wasn't.</em></li>
            </ul>

            <h3>2. Simple Past + Past Progressive juntos</h3>
            <ul>
              <li><span class="hl">Past Progressive</span> → ação em progresso (fundo).</li>
              <li><span class="hl">Simple Past</span> → ação que interrompe.</li>
              <li>Exemplo: <em>I <span class="hl">was running</span> to catch the bus when I <span class="hl">fell</span>.</em></li>
            </ul>

            <h3>3. When e While</h3>
            <ul>
              <li><span class="hl">When</span> → antes do <strong>Simple Past</strong>: <em>We saw the snake when we were sitting.</em></li>
              <li><span class="hl">While</span> → antes do <strong>Past Progressive</strong>: <em>We saw the snake while we were sitting.</em></li>
            </ul>

            <h3>4. Gerúndio (-ing)</h3>
            <p>Regras: <em>play → playing</em>; verbo em -e mudo → retira o e (<em>make → making</em>);
            consoante + vogal + consoante tônica → dobra (<em>chat → chatting</em>).</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Em respostas curtas, não repita o verbo em -ing: <em>Were you running? Yes, I was.</em>
            </div>""",
            "resumo": """
            <h3>Past Progressive</h3>
            <table>
              <thead><tr><th>Pessoa</th><th>Afirmativo</th><th>Negativo</th></tr></thead>
              <tbody>
                <tr><td>I / he / she / it</td><td>was + -ing</td><td>wasn't + -ing</td></tr>
                <tr><td>you / we / they</td><td>were + -ing</td><td>weren't + -ing</td></tr>
              </tbody>
            </table>

            <h3>When × While</h3>
            <table>
              <thead><tr><th>Conector</th><th>Usa com</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>when</td><td>Simple Past</td><td>…when my mom <span class="hl">arrived</span>.</td></tr>
                <tr><td>while</td><td>Past Progressive</td><td>…while I <span class="hl">was doing</span> homework.</td></tr>
              </tbody>
            </table>

            <h3>Combinação típica</h3>
            <p><em>She <span class="hl">was carrying</span> the groceries when she <span class="hl">dropped</span> the eggs.</em></p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Identifique qual ação estava em andamento (was/were + -ing) e qual a interrompeu (verbo no passado simples).
            </div>""",
            "dicas": """
            <ul>
              <li>Procure pistas de tempo: <em>when the teacher arrived</em>, <em>last night</em>, <em>yesterday</em>.</li>
              <li>A ação mais longa (em progresso) leva <strong>was/were + -ing</strong>.</li>
              <li>A ação rápida ou interruptora fica no <strong>Simple Past</strong> (forma regular ou irregular).</li>
              <li>Em exercícios de reescrita com <em>while</em>, coloque o -ing logo após o conector.</li>
              <li>Revise a forma -ing: <em>make → making</em>, <em>chat → chatting</em>.</li>
              <li>Leia o enunciado inteiro antes de escolher was ou were.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Complete: \"My sister ___ the groceries when she ___ the eggs.\"",
                ["was carrying / dropped", "carried / was dropping", "was carrying / was dropping", "carries / drops"],
                0,
                "Carregar era a ação em progresso (Past Progressive); derrubar interrompeu (Simple Past).",
                "Resposta correta: was carrying / dropped.",
            ),
            _mc(
                "Rewrite with \"while\": \"I was doing my homework. My mom arrived home.\"",
                [
                    "While I did my homework, my mom arrived.",
                    "While I was doing my homework, my mom arrived home.",
                    "While my mom arrived, I was doing homework.",
                    "I was doing while my mom arrived.",
                ],
                1,
                "While introduz o Past Progressive; a chegada da mãe fica no Simple Past.",
                "Resposta correta: While I was doing my homework, my mom arrived home.",
            ),
            _mc(
                "Qual frase está correta?",
                [
                    "When we were sitting, we saw the snake.",
                    "When we sat, we were seeing the snake.",
                    "While we saw the snake, we were sitting.",
                    "We were sitting when we were seeing the snake.",
                ],
                0,
                "When pode introduzir o Simple Past após a ação em progresso — ambas as ordens são possíveis, mas esta está gramaticalmente correta.",
                "Resposta correta: When we were sitting, we saw the snake.",
            ),
            _mc(
                "Complete: \"They ___ soccer when a dog ___ their ball.\"",
                ["were playing / took", "played / was taking", "were playing / was taking", "play / takes"],
                0,
                "Jogar bola = ação em andamento; o cachorro interrompeu levando a bola.",
                "Resposta correta: were playing / took.",
            ),
            _mc(
                "Qual é a forma -ing do verbo \"make\"?",
                ["makeing", "making", "makking", "maken"],
                1,
                "Verbos terminados em -e mudo perdem o e antes de -ing.",
                "Resposta correta: making.",
            ),
            _mc(
                "Short answer: \"Were you running at 6pm?\" — resposta afirmativa:",
                ["Yes, I were.", "Yes, I was running.", "Yes, I was.", "Yes, you were."],
                2,
                "Resposta curta: repete o sujeito + was/were, sem o verbo em -ing.",
                "Resposta correta: Yes, I was.",
            ),
            _sa(
                "Complete a frase: \"I ___ (listen) to music when my friend ___ (call) me.\" (Past Progressive + Simple Past)",
                ["was listening", "called", "listening", "call"],
                "Escuta = ação em progresso; ligação = interrupção.",
                "Resposta esperada: I was listening to music when my friend called me.",
            ),
            _mc(
                "No diálogo da revista Cool Life, Alicia estava ___ quando recebeu a ligação de Katia.",
                ["sleeping and not watching TV", "chatting online", "camping only", "winning the World Cup"],
                1,
                "Ela conversava online e ouvia música quando Katia ligou.",
                "Resposta correta: chatting online.",
            ),
        ],
    }


def _subject_geografia() -> dict:
    return {
        "title": "Geografia",
        "icon": "GE",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 9 — Climas do Brasil</strong>: zonas climáticas, latitude, temperatura média,
            influência do relevo e das <strong>massas de ar</strong>.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Brasil: país tropical</h3>
            <p>A maior parte do território brasileiro está na <span class="hl">Zona Tropical</span>
            (entre os trópicos). Apenas o Sul está na Zona Temperada. Paralelos importantes:
            <strong>Equador</strong> e <strong>Trópico de Capricórnio</strong>.</p>

            <h3>2. Latitude e temperatura</h3>
            <p>Quanto <strong>menor</strong> a latitude (mais perto do Equador), em geral <strong>maior</strong> a temperatura média.
            Exemplo: Macapá (27 °C) &gt; Florianópolis (20 °C).</p>

            <h3>3. Influência do relevo (altitude)</h3>
            <p>Em cidades na mesma latitude, quanto <strong>maior a altitude</strong>, <strong>menor</strong> a temperatura.
            Campos do Jordão (1 640 m → 13,6 °C) é mais frio que Paraty (5 m → 23,3 °C).</p>

            <h3>4. Massas de ar no Brasil</h3>
            <table>
              <thead><tr><th>Sigla</th><th>Origem</th><th>Característica</th></tr></thead>
              <tbody>
                <tr><td>mEc</td><td>Amazônia ocidental</td><td>Quente e muito úmida</td></tr>
                <tr><td>mEa</td><td>Atlântico Norte</td><td>Quente e úmida</td></tr>
                <tr><td>mTc</td><td>América do Sul central</td><td>Quente e seca</td></tr>
                <tr><td>mTa</td><td>Atlântico Sul</td><td>Quente e muito úmida</td></tr>
                <tr><td>mPa</td><td>Atlântico Sul (ar polar)</td><td>Fria e seca</td></tr>
              </tbody>
            </table>

            <h3>5. Ação da mPa no inverno</h3>
            <ul>
              <li><strong>Caminho A:</strong> friagem na Amazônia meridional.</li>
              <li><strong>Caminho B:</strong> geadas no Sul e Sudeste.</li>
              <li><strong>Caminho C:</strong> chuvas no litoral nordestino (encontro com mTa).</li>
            </ul>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Fatores do clima: latitude, altitude, massas de ar, correntes marítimas, maritimidade e continentalidade.
            </div>""",
            "resumo": """
            <h3>Zonas climáticas</h3>
            <table>
              <thead><tr><th>Zona</th><th>Localização</th><th>Brasil</th></tr></thead>
              <tbody>
                <tr><td>Tropical</td><td>Entre os trópicos</td><td>Maior parte do país</td></tr>
                <tr><td>Temperada</td><td>Entre trópico e círculo polar</td><td>Região Sul</td></tr>
              </tbody>
            </table>

            <h3>Temperatura × latitude (exemplos)</h3>
            <table>
              <thead><tr><th>Cidade</th><th>Temp. média</th></tr></thead>
              <tbody>
                <tr><td>Macapá (AP)</td><td>27,0 °C</td></tr>
                <tr><td>Salvador (BA)</td><td>25,2 °C</td></tr>
                <tr><td>Rio de Janeiro (RJ)</td><td>23,2 °C</td></tr>
                <tr><td>Florianópolis (SC)</td><td>20,1 °C</td></tr>
              </tbody>
            </table>

            <h3>Massas de ar — síntese</h3>
            <p>mEc/mEa/mTa = úmidas · mTc = seca · mPa = fria (inverno: friagem, geadas, chuvas no NE).</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Altitude também reduz a temperatura — não confunda só com latitude!
            </div>""",
            "dicas": """
            <ul>
              <li>Em mapas de temperatura, observe a cor e a posição em relação ao Equador.</li>
              <li>Massa Tropical Continental (mTc) traz <strong>seca</strong>; Equatorial/Atlântica trazem <strong>chuva</strong>.</li>
              <li>Friagem = queda brusca de temperatura no Norte quando a mPa avança (caminho A).</li>
              <li>Geadas em Santa Maria (RS) ilustram o inverno mais frio no Sul.</li>
              <li>Relacione paralelos (Equador, Trópico de Capricórnio) com zonas climáticas.</li>
              <li>Compare cidades na mesma latitude mas altitudes diferentes (Campos do Jordão × Paraty).</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "A maior parte do Brasil está em qual zona climática?",
                ["Glacial", "Temperada", "Tropical", "Polar"],
                2,
                "O país está majoritariamente entre os trópicos — Zona Tropical.",
                "Resposta correta: Tropical.",
            ),
            _mc(
                "Qual paralelo importante cruza o Brasil além do Equador?",
                ["Trópico de Câncer", "Trópico de Capricórnio", "Círculo Polar", "Meridiano de Greenwich"],
                1,
                "O Trópico de Capricórnio passa pelo Sul do Brasil.",
                "Resposta correta: Trópico de Capricórnio.",
            ),
            _mc(
                "Entre Macapá e Florianópolis, qual tende a ter temperatura média mais alta?",
                ["Florianópolis — mais ao sul", "Macapá — mais próxima do Equador", "Iguais", "Depende só do relevo"],
                1,
                "Macapá está mais perto do Equador → maior incidência solar → temperatura mais alta.",
                "Resposta correta: Macapá.",
            ),
            _mc(
                "Campos do Jordão é mais fria que Paraty porque:",
                ["Está mais ao norte", "Tem maior altitude", "Recebe só mTc", "Fica no litoral"],
                1,
                "Ambas na mesma latitude, mas Campos do Jordão tem 1 640 m de altitude.",
                "Resposta correta: tem maior altitude.",
            ),
            _mc(
                "A massa de ar mTc é caracterizada por ser:",
                ["Quente e seca", "Quente e muito úmida", "Fria e seca", "Fria e úmida"],
                0,
                "mTc = Tropical Continental — quente e seca, origem no interior da América do Sul.",
                "Resposta correta: quente e seca.",
            ),
            _mc(
                "No inverno, a massa Polar Atlântica (mPa) pode causar geadas principalmente no caminho:",
                ["A — Amazônia", "B — Sul e Sudeste", "C — litoral nordestino", "Nenhum"],
                1,
                "Caminho B: mPa avança pelo Sul/Sudeste provocando queda de temperatura e geadas.",
                "Resposta correta: B — Sul e Sudeste.",
            ),
            _mc(
                "O fenômeno de queda brusca de temperatura na Amazônia meridional no inverno chama-se:",
                ["El Niño", "Friagem", "Maré", "Continentalidade"],
                1,
                "Friagem = efeito da mPa avançando pelo caminho A.",
                "Resposta correta: friagem.",
            ),
            _sa(
                "Cite dois fatores que influenciam o clima brasileiro estudados no Módulo 9.",
                ["latitude", "altitude", "massas de ar", "relevo"],
                "Latitude, altitude e massas de ar são fatores centrais do módulo.",
                "Resposta esperada: latitude e altitude (ou massas de ar).",
            ),
        ],
    }


def _subject_matematica() -> dict:
    return {
        "title": "Matemática",
        "icon": "MA",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 23 — Expressões numéricas</strong>: ordem das operações,
            parênteses, potenciação e problemas com números decimais.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. O que é uma expressão numérica?</h3>
            <p>Sequência de duas ou mais operações com números naturais ou racionais.
            A ordem importa: <em>50 − 2 × 16</em> não é igual se você subtrair antes de multiplicar!</p>

            <h3>2. Ordem das operações (sem parênteses)</h3>
            <ol>
              <li>Primeiro: <span class="hl">multiplicação</span> e <span class="hl">divisão</span> (da esquerda para a direita).</li>
              <li>Depois: <span class="hl">adição</span> e <span class="hl">subtração</span> (da esquerda para a direita).</li>
            </ol>
            <p>Exemplo: <em>50 − 2 × 16 = 50 − 32 = 18</em> (correto).</p>

            <h3>3. Parênteses</h3>
            <p>Operações <strong>dentro dos parênteses</strong> vêm primeiro, seguindo a mesma ordem interna.
            Exemplo: <em>50 − (12 + 3 × 10) = 50 − 42 = 8</em>.</p>

            <h3>4. Potenciação</h3>
            <p>Resolve-se antes da multiplicação/divisão quando se aplica a um número só.
            <em>16 + 2³ = 16 + 8 = 24</em>. Se a potência envolve expressão: <em>(2 + 3 × 2)²</em> → resolve dentro, depois eleva.</p>

            <h3>5. Problemas do cotidiano</h3>
            <p>Traduzir situações em expressões: troco, divisão de livros, brigadeiros em bandejas, lanches pagos com nota de R$ 50.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Multiplicação e divisão têm prioridade sobre adição e subtração — salvo se parênteses mudarem a ordem.
            </div>""",
            "resumo": """
            <h3>Ordem das operações</h3>
            <table>
              <thead><tr><th>Prioridade</th><th>Operações</th></tr></thead>
              <tbody>
                <tr><td>1ª</td><td>Parênteses (por dentro)</td></tr>
                <tr><td>2ª</td><td>Potenciação (quando aplicável)</td></tr>
                <tr><td>3ª</td><td>× e ÷ (esquerda → direita)</td></tr>
                <tr><td>4ª</td><td>+ e − (esquerda → direita)</td></tr>
              </tbody>
            </table>

            <h3>Exemplos</h3>
            <ul>
              <li><em>4,5 + 2 × 1,5 = 4,5 + 3 = 7,5</em></li>
              <li><em>48 + 42 ÷ 3 = 48 + 14 = 62</em></li>
              <li><em>50 − (12 + 3 × 10) = 50 − 42 = 8</em></li>
              <li><em>16 + 2³ = 16 + 8 = 24</em></li>
            </ul>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              <em>48 ÷ 2 × 0,5</em> → resolve × e ÷ na ordem: 24 × 0,5 = 12.
            </div>""",
            "dicas": """
            <ul>
              <li>Em problemas, identifique o que calcular primeiro (total gasto? troco? divisão?).</li>
              <li>Parênteses mudam tudo — resolva o interior antes de multiplicar/dividir por fora.</li>
              <li>Potência de número único vem antes da multiplicação: <em>25 − 48 ÷ 2²</em> → calcule 2² primeiro.</li>
              <li>Com decimais, use a mesma ordem — cuidado com vírgula no final.</li>
              <li>Releia o enunciado: «quanto sobrou?» geralmente é subtração no final.</li>
              <li>Teste se o resultado faz sentido no contexto (troco não pode ser maior que o pagamento).</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Qual é o valor de 50 − 2 × 16?",
                ["768", "18", "32", "48"],
                1,
                "Primeiro 2 × 16 = 32; depois 50 − 32 = 18.",
                "Resposta correta: 18.",
            ),
            _mc(
                "Calcule: 4,5 + 2 × 1,5",
                ["9", "7,5", "10,5", "6"],
                1,
                "2 × 1,5 = 3; 4,5 + 3 = 7,5.",
                "Resposta correta: 7,5.",
            ),
            _mc(
                "Calcule: 50 − (12 + 3 × 10)",
                ["8", "380", "42", "20"],
                0,
                "Dentro: 3 × 10 = 30; 12 + 30 = 42; 50 − 42 = 8.",
                "Resposta correta: 8.",
            ),
            _mc(
                "Calcule: 16 + 2³",
                ["24", "18", "64", "8"],
                0,
                "2³ = 8; 16 + 8 = 24.",
                "Resposta correta: 24.",
            ),
            _mc(
                "Marcos tinha R$ 20 e recebeu R$ 48 da avó para dividir igualmente com o irmão. Quanto ele tem no total?",
                ["R$ 44", "R$ 68", "R$ 48", "R$ 24"],
                0,
                "Metade de 48 = 24; 20 + 24 = 44.",
                "Resposta correta: R$ 44.",
            ),
            _mc(
                "52 livros doados: 15 para cada uma das duas turmas do 6º ano. Quantos vão para a biblioteca?",
                ["22", "30", "37", "7"],
                0,
                "15 + 15 = 30 para as turmas; 52 − 30 = 22 para a biblioteca.",
                "Resposta correta: 22.",
            ),
            _mc(
                "Ana comprou 2 caixas com 75 brigadeiros e dividirá igualmente em 6 bandejas. Quantos por bandeja?",
                ["25", "150", "12", "75"],
                0,
                "2 × 75 = 150; 150 ÷ 6 = 25.",
                "Resposta correta: 25.",
            ),
            _mc(
                "Dois lanches (R$ 10,50 cada) + duas vitaminas (R$ 7,20 cada). Pagou com R$ 50. Troco?",
                ["R$ 14,40", "R$ 35,60", "R$ 35,40", "R$ 14,60"],
                3,
                "Gasto: 2×10,50 + 2×7,20 = 21 + 14,40 = 35,40; troco = 50 − 35,40 = 14,60.",
                "Resposta correta: R$ 14,60.",
            ),
            _sa(
                "Calcule: 7,5 − 5 ÷ 2,5",
                ["5.5", "5,5", "5.50"],
                "Primeiro 5 ÷ 2,5 = 2; 7,5 − 2 = 5,5.",
                "Resposta esperada: 5,5.",
            ),
        ],
    }


def _subject_desenho() -> dict:
    return {
        "title": "Desenho Geométrico",
        "icon": "DG",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 12</strong> (Geometria): retas <strong>paralelas</strong>,
            <strong>concorrentes</strong> e <strong>perpendiculares</strong>; notação // e ⊥; retângulos e sólidos.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Retas paralelas</h3>
            <p>Duas retas no mesmo plano que <strong>nunca se cruzam</strong> — não têm ponto em comum.
            Notação: <span class="hl">r // s</span>.</p>

            <h3>2. Retas concorrentes</h3>
            <p>Retas que têm <strong>exatamente um ponto</strong> em comum (se cruzam).</p>

            <h3>3. Retas perpendiculares</h3>
            <p>Tipo especial de concorrentes: formam <strong>ângulos retos</strong> (90°) ao se cruzar.
            Notação: <span class="hl">r ⊥ s</span>. Símbolo: quadradinho no encontro.</p>

            <h3>4. Retângulo</h3>
            <ul>
              <li>Lados opostos (<em>EF // GH</em>, <em>FG // EH</em>) são <strong>paralelos</strong>.</li>
              <li>Lados adjacentes (<em>EF</em> e <em>FH</em>) são <strong>concorrentes</strong> e <strong>perpendiculares</strong>.</li>
              <li>Diagonais (<em>EG</em> e <em>FH</em>) são <strong>concorrentes</strong>, mas <strong>não perpendiculares</strong> (em geral).</li>
            </ul>

            <h3>5. Paralelepípedo (caixote)</h3>
            <p>Arestas paralelas em faces opostas: <em>AB // DE</em>. Arestas de faces adjacentes são perpendiculares.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Toda reta perpendicular é concorrente, mas nem toda concorrente é perpendicular.
            </div>""",
            "resumo": """
            <h3>Tipos de retas</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Definição</th><th>Símbolo</th></tr></thead>
              <tbody>
                <tr><td>Paralelas</td><td>Nunca se cruzam</td><td>//</td></tr>
                <tr><td>Concorrentes</td><td>1 ponto em comum</td><td>—</td></tr>
                <tr><td>Perpendiculares</td><td>Concorrentes com 90°</td><td>⊥</td></tr>
              </tbody>
            </table>

            <h3>Retângulo EFGH</h3>
            <p><em>EF // GH</em> · <em>EF ⊥ FH</em> · diagonais concorrentes, não perpendiculares.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Diagonais de um retângulo se cruzam, mas não formam 90° (salvo no quadrado).
            </div>""",
            "dicas": """
            <ul>
              <li>Paralelas = mesma direção, nunca se encontram (como trilhos de trem).</li>
              <li>Perpendiculares = formam «L» perfeito (90°) — procure o quadradinho no desenho.</li>
              <li>Em paralelepípedos, arestas de faces diferentes adjacentes são perpendiculares.</li>
              <li>Diagonal ≠ lado — não confunda paralelismo de diagonais com lados.</li>
              <li>Para traçar com precisão, use régua e esquadro (não desenho à mão livre).</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Duas retas no mesmo plano que nunca se cruzam são:",
                ["Concorrentes", "Paralelas", "Perpendiculares", "Coincidentes"],
                1,
                "Paralelas não têm ponto em comum e não se cruzam.",
                "Resposta correta: paralelas.",
            ),
            _mc(
                "Retas perpendiculares ao se cruzarem formam:",
                ["Ângulos agudos", "Ângulos retos (90°)", "Nenhum ângulo", "Linhas curvas"],
                1,
                "Perpendiculares formam 90° — ângulos retos.",
                "Resposta correta: ângulos retos (90°).",
            ),
            _mc(
                "No retângulo EFGH, os lados EF e GH são:",
                ["Perpendiculares", "Paralelos", "Concorrentes obliquas", "Coincidentes"],
                1,
                "Lados opostos de um retângulo são paralelos.",
                "Resposta correta: paralelos.",
            ),
            _mc(
                "No retângulo EFGH, as retas EF e FH são:",
                ["Paralelas", "Concorrentes e perpendiculares", "Paralelas e perpendiculares", "Nunca se cruzam"],
                1,
                "Lados adjacentes se cruzam em 90° — concorrentes e perpendiculares.",
                "Resposta correta: concorrentes e perpendiculares.",
            ),
            _mc(
                "No paralelepípedo, AB e DE são:",
                ["Perpendiculares", "Paralelas", "Diagonais", "Curvas"],
                1,
                "Arestas opostas em faces paralelas do sólido são paralelas.",
                "Resposta correta: paralelas.",
            ),
            _mc(
                "O símbolo ⊥ indica retas:",
                ["Paralelas", "Perpendiculares", "Coincidentes", "Secantes obliquas"],
                1,
                "⊥ = perpendicular.",
                "Resposta correta: perpendiculares.",
            ),
        ],
    }


def _subject_ciencias() -> dict:
    return {
        "title": "Ciências",
        "icon": "CI",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 13 — Poluição e desperdício de água</strong>: distribuição da água na Terra,
            poluição, água virtual, cisternas e poluição térmica.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Água na Terra</h3>
            <p>96,5% é <strong>salobra</strong> (oceanos). Apenas 3,5% é água doce — e a maior parte está
            em <strong>glaciares</strong> (68,7% da doce) ou <strong>subterrânea</strong> (30,1%).
            Água superficial (rios, lagos) = fração mínima (~0,3%).</p>

            <h3>2. Uso da água doce</h3>
            <ul>
              <li><strong>Irrigação</strong> → ~70% (Brasil: 68,4%).</li>
              <li><strong>Indústrias</strong> → ~22%.</li>
              <li><strong>Residências</strong> → ~8%.</li>
            </ul>

            <h3>3. Poluição da água</h3>
            <p>Esgoto doméstico e resíduos industriais despejados sem tratamento contaminam rios, lagos e mares.
            Água poluída recebe substâncias que a tornam imprópria: esgoto, toxinas, bactérias.</p>

            <h3>4. Poluição térmica</h3>
            <p>Indústrias despejam água <strong>aquecida</strong> (usinas, siderúrgicas, nucleares).
            Aquecer a água <strong>reduz o oxigênio dissolvido</strong> → prejudica peixes e organismos aquáticos.</p>

            <h3>5. Desperdício e água virtual</h3>
            <p><strong>Água virtual</strong> = água usada para produzir alimentos e produtos exportados
            (ex.: Brasil exporta «água» embutida em commodities). <strong>Cisternas</strong> no Semiárido
            captam água da chuva.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              A água parece abundante, mas a disponível para consumo é escassa — por isso poluição e desperdício são graves.
            </div>""",
            "resumo": """
            <h3>Distribuição da água</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Proporção</th></tr></thead>
              <tbody>
                <tr><td>Salobra (oceanos)</td><td>96,5%</td></tr>
                <tr><td>Doce total</td><td>3,5%</td></tr>
                <tr><td>Doce em glaciares</td><td>68,7% da doce</td></tr>
                <tr><td>Doce subterrânea</td><td>30,1% da doce</td></tr>
                <tr><td>Doce superficial</td><td>~0,3%</td></tr>
              </tbody>
            </table>

            <h3>Poluição</h3>
            <p>Esgoto + resíduos industriais · poluição térmica (menos O₂) · falta de saneamento.</p>

            <h3>Água virtual</h3>
            <p>Água «embutida» na produção de bens exportados — não vai em galões, mas nos produtos.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Irrigação é o maior consumidor de água doce no Brasil e no mundo.
            </div>""",
            "dicas": """
            <ul>
              <li>Memorize: quase toda água do planeta é salgada; doce disponível é mínima.</li>
              <li>Poluição térmica ≠ poluição química — mas ambas prejudicam a vida aquática.</li>
              <li>Água virtual explica por que países «importam água» sem receber galões.</li>
              <li>Cisternas = solução no Semiárido para captar chuva.</li>
              <li>Desperdício: torneiras pingando, canos quebrados, hábitos irresponsáveis.</li>
              <li>Relacione esgoto sem tratamento com doenças e contaminação de mananciais.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Qual porcentagem da água do planeta é salobra?",
                ["3,5%", "50%", "96,5%", "68,7%"],
                2,
                "96,5% está nos oceanos — água salgada.",
                "Resposta correta: 96,5%.",
            ),
            _mc(
                "A maior parte da água doce está em:",
                ["Rios", "Glaciares", "Lagos", "Reservatórios urbanos"],
                1,
                "68,7% da água doce está em glaciares (estado sólido).",
                "Resposta correta: glaciares.",
            ),
            _mc(
                "No mundo, a maior parte da água doce consumida é usada em:",
                ["Residências", "Indústrias", "Irrigação agrícola", "Bebidas"],
                2,
                "Cerca de 70% vai para irrigação.",
                "Resposta correta: irrigação agrícola.",
            ),
            _mc(
                "Poluição térmica ocorre quando indústrias despejam água aquecida, reduzindo:",
                ["A salinidade", "O oxigênio dissolvido", "A densidade do ar", "A massa dos peixes"],
                1,
                "Água quente dissolve menos oxigênio — organismos aquáticos sofrem.",
                "Resposta correta: oxigênio dissolvido.",
            ),
            _mc(
                "Água virtual é:",
                ["Água embalada em galões para exportação", "Água usada na produção de bens e alimentos", "Chuva ácida", "Gelo derretido"],
                1,
                "É a água consumida/indireta na produção — não vai em contêineres de galões.",
                "Resposta correta: água usada na produção de bens e alimentos.",
            ),
            _mc(
                "Cisternas no Semiárido brasileiro servem para:",
                ["Despejar esgoto", "Captar e armazenar água da chuva", "Aquecer água industrial", "Gerar eletricidade"],
                1,
                "Calhas direcionam a chuva para cisternas — combate à escassez.",
                "Resposta correta: captar e armazenar água da chuva.",
            ),
            _mc(
                "Principal fonte de poluição da água doce no Brasil, segundo o material:",
                ["Poluição luminosa", "Esgoto doméstico sem tratamento", "Vulcões", "Marés"],
                1,
                "Esgoto despejado sem tratamento contamina rios e lençóis.",
                "Resposta correta: esgoto doméstico sem tratamento.",
            ),
            _sa(
                "Por que dizemos que a água doce disponível é um bem escasso?",
                ["escassa", "pouca", "glaciares", "superficial"],
                "Pouca água doce, e a maior parte não está acessível (glaciares/subterrânea).",
                "Resposta esperada: porque só 3,5% é doce e quase toda está em glaciares ou underground, restando muito pouca superficial.",
            ),
        ],
    }


def _subject_portugues() -> dict:
    return {
        "title": "Língua Portuguesa",
        "icon": "PT",
        "sections": {
            "percurso": f"""
            <p>Conteúdo dos <strong>Módulos 29 e 32</strong>: conectores textuais, acentuação de oxítonas,
            textos verbais e não verbais e interpretação de textos.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Conectores textuais</h3>
            <p>Palavras ou expressões que <strong>unem</strong> frases, períodos e parágrafos, garantindo
            <span class="hl">coesão</span> e progressão das ideias. Sem conectores, temos apenas «amontoado de palavras».</p>
            <ul>
              <li><span class="hl">e</span> → adição</li>
              <li><span class="hl">mas</span> → oposição</li>
              <li><span class="hl">porque / visto que</span> → causa</li>
              <li><span class="hl">para</span> → finalidade</li>
              <li><span class="hl">enquanto</span> → tempo</li>
              <li><span class="hl">por isso</span> → conclusão/consequência</li>
            </ul>
            <p>Podem ser <strong>conjunções</strong>, <strong>preposições</strong> ou <strong>advérbios</strong> — o sentido depende do contexto.</p>

            <h3>2. Repetição como recurso coesivo</h3>
            <p>Repetir palavras sem critério prejudica a coesão. Repetição <strong>intencional</strong>
            (ex.: «depois», «vinte e oito anos depois») pode enfatizar ideia — como a lentidão em «O abridor de latas».</p>

            <h3>3. Acentuação de oxítonas</h3>
            <p>Palavras oxítonas têm a sílaba tônica na <strong>última</strong>. Regra:</p>
            <ul>
              <li>Terminadas em <strong>A, E, O</strong> → agudas (sem acento): <em>café</em>… oxítonas em -a, -e, -o átonos: <em>você</em> (exceção).</li>
              <li>Terminadas em <strong>-em, -ens</strong> → agudas: <em> também</em>.</li>
              <li>Regra prática 6º ano: oxítonas terminadas em <strong>i, u</strong> (paroxítonas na verdade — cuidado!)…</li>
            </ul>
            <p><strong>Oxítonas acentuadas:</strong> terminadas em <strong>-á, -é, -í, -ó, -ú</strong> (tônica na última, vogal aberta/fechada acentuada):
            <em>café, cajú, baú, herói, cipó</em>.</p>
            <p><strong>Oxítonas sem acento:</strong> terminadas em <strong>-a, -e, -o</strong> átonos: <em>lápis</em> (paroxítona), <em>você</em> (proparoxítona).</p>

            <h3>4. Textos verbais e não verbais</h3>
            <ul>
              <li><strong>Verbal:</strong> usa <strong>linguagem escrita</strong> (palavras) como principal meio — contos, reportagens, poemas.</li>
              <li><strong>Não verbal:</strong> usa <strong>imagens, gestos, sons, gráficos</strong> — cartazes, mapas, infográficos, charges.</li>
              <li><strong>Texto misto:</strong> combina verbal + não verbal (ex.: reportagem com fotos e legendas).</li>
            </ul>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Conectores garantem que o leitor perceba a relação entre as ideias (causa, oposição, tempo, conclusão).
            </div>""",
            "resumo": """
            <h3>Conectores — funções</h3>
            <table>
              <thead><tr><th>Conector</th><th>Função</th></tr></thead>
              <tbody>
                <tr><td>e</td><td>Adição</td></tr>
                <tr><td>mas</td><td>Oposição</td></tr>
                <tr><td>porque / visto que</td><td>Causa</td></tr>
                <tr><td>para</td><td>Finalidade</td></tr>
                <tr><td>enquanto</td><td>Tempo</td></tr>
                <tr><td>por isso</td><td>Consequência</td></tr>
              </tbody>
            </table>

            <h3>Oxítonas — acento</h3>
            <p>Acentuam-se oxítonas em <span class="hl">-á, -é, -í, -ó, -ú</span>: <em>café, baú, herói</em>.</p>

            <h3>Verbal × Não verbal</h3>
            <p>Verbal = palavras · Não verbal = imagens/gráficos · Misto = os dois.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Identifique o conector pelo <strong>sentido</strong> da frase, não só pela classe gramatical.
            </div>""",
            "dicas": """
            <ul>
              <li>Substitua o conector por sinônimo (porém, contudo) para testar oposição.</li>
              <li>Em «O abridor de latas», «mas» contrasta ideias — marque o que vem antes e depois.</li>
              <li>Oxítona = tônica na última sílaba — conte de trás para frente.</li>
              <li>Infográfico de água = texto não verbal (ou misto se tiver legendas).</li>
              <li>Interpretação: leia título, imagens e conectores antes das alternativas.</li>
              <li>Repetição estilística ≠ repetição por descuido — observe se reforça um tema.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Em «Passaram-se cinquenta anos e a tartaruga não apareceu», o conector é:",
                ["mas", "e", "porque", "enquanto"],
                1,
                "«e» liga as duas orações adicionando informação.",
                "Resposta correta: e.",
            ),
            _mc(
                "O conector «mas» em «O abridor de latas» indica:",
                ["Causa", "Oposição", "Tempo", "Finalidade"],
                1,
                "«Mas» contrasta ou opõe ideias entre trechos do texto.",
                "Resposta correta: oposição.",
            ),
            _mc(
                "«Visto que» é conector de:",
                ["Adição", "Causa", "Conclusão", "Comparação"],
                1,
                "Visto que = dado que = porque → causa.",
                "Resposta correta: causa.",
            ),
            _mc(
                "Qual palavra oxítona está acentuada corretamente?",
                ["cafe", "café", "cáfe", "cafê"],
                1,
                "Oxítona terminada em -é (vogal aberta) leva acento: café.",
                "Resposta correta: café.",
            ),
            _mc(
                "«Baú» leva acento porque é oxítona terminada em:",
                ["-a", "-u", "-i", "-o"],
                1,
                "Oxítonas terminadas em -ú (u tônico) levam acento: baú.",
                "Resposta correta: -u.",
            ),
            _mc(
                "Um cartaz só com imagens e setas, sem palavras, é texto:",
                ["Verbal", "Não verbal", "Poético", "Jornalístico"],
                1,
                "Sem linguagem escrita predominante → não verbal.",
                "Resposta correta: não verbal.",
            ),
            _mc(
                "Reportagem com fotos e parágrafos explicativos é texto:",
                ["Só verbal", "Só não verbal", "Misto (verbal e não verbal)", "Nenhum"],
                2,
                "Combina palavras (verbal) e imagens (não verbal).",
                "Resposta correta: misto.",
            ),
            _sa(
                "Cite um conector de tempo usado no Módulo 29.",
                ["enquanto", "depois", "quando", "aí"],
                "Enquanto, depois, aí marcam tempo ou sequência.",
                "Resposta esperada: enquanto (ou depois, aí).",
            ),
        ],
    }


def _subject_espanhol() -> dict:
    return {
        "title": "Espanhol",
        "icon": "ES",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 8 — ¿Nosotros comemos?</strong>: alimentação, verbos regulares no presente,
            verbo <span class="hl">gustar</span>, pronúncia de G e J, fome como problema social.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Verbos regulares no presente</h3>
            <p>Terminações: <strong>-ar</strong> (estudi<strong>ar</strong> → estudi<strong>o</strong>, estudi<strong>as</strong>…),
            <strong>-er</strong>, <strong>-ir</strong>. Verbos irregulares importantes: <span class="hl">ser</span>, <span class="hl">tener</span>.</p>

            <h3>2. Gustar + pronome oblíquo</h3>
            <p>Em espanhol, «gostar» concorda com a <strong>coisa gostada</strong> (singular/plural):</p>
            <ul>
              <li><em>A mí me gusta la tortilla.</em> (singular)</li>
              <li><em>A mí no me gustan los pescados.</em> (plural → gustan)</li>
            </ul>
            <p>Pronomes: <span class="hl">me, te, le, nos, os, les</span>.</p>

            <h3>3. Vocabulário — alimentação</h3>
            <p><strong>Desayuno:</strong> pan, leche… · <strong>Almuerzo/cena:</strong> carne, pescado, sopa, ensalada, pasta…
            · <strong>Postre:</strong> frutas, chocolate…</p>

            <h3>4. Tema social: fome e direito à alimentação</h3>
            <p>Textos de Oche Califa («A pesar de todo») e poema de Gloria Fuertes («Niños de Somalia») abordam
            pobreza e fome. Verbo <span class="hl">comer</span>: <em>yo como, tú comes, ellos no (comen)</em>.</p>

            <h3>5. Pronúncia de G e J</h3>
            <p>Antes de <strong>e, i</strong> → som mais forte (já, juego). Antes de <strong>a, o, u</strong> → som de /g/ (gato, gusto).</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Com «gustar», o sujeito gramatical é a coisa gostada: «Me gustan las manzanas» = literalmente «As maçãs agradam-me».
            </div>""",
            "resumo": """
            <h3>Gustar</h3>
            <table>
              <thead><tr><th>Pessoa</th><th>Pronome</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>yo</td><td>me</td><td>Me gusta el chocolate.</td></tr>
                <tr><td>tú</td><td>te</td><td>¿Te gustan las manzanas?</td></tr>
                <tr><td>él/ella</td><td>le</td><td>Le gusta la tortilla.</td></tr>
                <tr><td>nosotros</td><td>nos</td><td>Nos gustan los pájaros.</td></tr>
                <tr><td>ellos</td><td>les</td><td>Les gusta mucho el chocolate.</td></tr>
              </tbody>
            </table>

            <h3>Comer (presente)</h3>
            <p><em>Yo como · Tú comes · Él come · Nosotros comemos · Vosotros coméis · Ellos no (comen)</em></p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              «Ellos no» no poema = eles não comem — referência aos niños de Somalia.
            </div>""",
            "dicas": """
            <ul>
              <li>Olhe se a coisa gostada é singular (gusta) ou plural (gustan).</li>
              <li>Não confunda «tener» (ter) com «ser» (ser): «Mi hermana tiene seis años».</li>
              <li>Em leitura, identifique o yo poético — não é sempre o autor real.</li>
              <li>Paródia = texto baseado em outro, com tom crítico ou irônico.</li>
              <li>Villa = assentamento precário (como favela); mate cocido = infusão tradicional.</li>
              <li>Classifique alimentos: desayuno / almuerzo / postre.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Complete: «A Mónica ___ gusta la tortilla.»",
                ["me", "le", "te", "les"],
                1,
                "Para «ella/Mónica» usa-se le: A Mónica le gusta…",
                "Resposta correta: le.",
            ),
            _mc(
                "«A mí no ___ gustan los pescados.»",
                ["le", "me", "te", "les"],
                1,
                "A mí → me (1ª pessoa do singular).",
                "Resposta correta: me.",
            ),
            _mc(
                "«Mi hermana menor ___ seis años.» (verbo ter)",
                ["es", "tiene", "estudia", "gusta"],
                1,
                "Idade → tener: tiene seis años.",
                "Resposta correta: tiene.",
            ),
            _mc(
                "No poema «Niños de Somalia», «Ellos no» significa que eles:",
                ["Comem muito", "Não comem", "Gostam de comer", "Cozinham"],
                1,
                "Contraste: «Nosotros comemos… ¡Ellos no!» — eles não comem.",
                "Resposta correta: não comem.",
            ),
            _mc(
                "«A los niños ___ gusta mucho el chocolate.»",
                ["le", "les", "me", "os"],
                1,
                "Los niños (plural) → les.",
                "Resposta correta: les.",
            ),
            _mc(
                "Mate cocido é uma infusão tradicional de países como:",
                ["Somente México", "Paraguai, Argentina, Brasil e Uruguai", "Somente Espanha", "Somente Chile"],
                1,
                "O texto cita Paraguai, Argentina, Brasil, Uruguai e Chile.",
                "Resposta correta: Paraguai, Argentina, Brasil e Uruguai.",
            ),
        ],
    }


def _subject_historia() -> dict:
    return {
        "title": "História",
        "icon": "HI",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 11 — O Egito antigo</strong>: origens no Vale do Nilo, cheia e vazante,
            nomos, unificação, faraós e agricultura.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Origens (c. 4000 a.C.)</h3>
            <p>Tribos nômades do Saara e da Península Arábica migraram para o <strong>Vale do Nilo</strong>,
            sedentarizaram-se, criaram aldeias e praticaram agricultura.</p>

            <h3>2. Importância do Nilo</h3>
            <ul>
              <li><strong>Cheia</strong> (julho a outubro): rio transborda.</li>
              <li><strong>Vazante</strong> (novembro a março): rio retorna; deixa <span class="hl">húmus</span> (solo fértil — «terra negra»).</li>
              <li><strong>Delta</strong>: desembocadura triangular no Mediterrâneo.</li>
            </ul>
            <p>Sem o Nilo, o Egito seria continuação do deserto.</p>

            <h3>3. Organização e unificação</h3>
            <p>Vilarejos formaram <strong>nomos</strong> (≈42), governados por <strong>nomarcas</strong>.
            Por volta de <strong>3200 a.C.</strong>, <strong>Menés</strong> unificou Alto e Baixo Egito — primeiro faraó.</p>

            <h3>4. Ciclo agrícola (Nilo)</h3>
            <ul>
              <li>Inundação → julho a outubro</li>
              <li>Semeadura → novembro a fevereiro</li>
              <li>Colheita → março a junho</li>
            </ul>

            <h3>5. Poder dos faraós</h3>
            <p>Donos das terras, representantes dos deuses, controlavam leis, defesa, colheitas e impostos.
            Fontes: múmias, miniaturas de túmulos, pinturas rupestres/túmulos.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              «Egito» significa «terra negra» — referência ao solo fértil deixado pelas cheias.
            </div>""",
            "resumo": """
            <h3>Linha do tempo</h3>
            <table>
              <thead><tr><th>Data</th><th>Evento</th></tr></thead>
              <tbody>
                <tr><td>c. 4000 a.C.</td><td>Sedentarização no Nilo</td></tr>
                <tr><td>c. 3200 a.C.</td><td>Unificação por Menés</td></tr>
              </tbody>
            </table>

            <h3>Nilo — cheia e vazante</h3>
            <p>Cheia deposita húmus → agricultura → civilização. Canais de irrigação ampliaram áreas cultiváveis.</p>

            <h3>Termos</h3>
            <p><strong>Nomo</strong> · <strong>Nomarca</strong> · <strong>Faraó</strong> · <strong>Delta</strong> · <strong>Húmus</strong></p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Pirâmides e Esfinge = símbolos do poder faraônico e da engenharia egípcia.
            </div>""",
            "dicas": """
            <ul>
              <li>Relacione cheia do Nilo com fertilidade e calendário agrícola.</li>
              <li>Menés = unificação Alto + Baixo Egito (≈3200 a.C.).</li>
              <li>Faraó = poder político + religioso (representante dos deuses).</li>
              <li>Fontes históricas: múmias, pinturas, miniaturas — «De olho na fonte».</li>
              <li>Delta = forma triangular na foz do Nilo (letra grega Δ).</li>
              <li>Em interpretação de Eça de Queirós, sublinhe cheia (lama, vivifica) e vazante.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Por volta de qual período grupos sedentarizaram-se no Vale do Nilo?",
                ["1500 d.C.", "4000 a.C.", "1937", "3200 d.C."],
                1,
                "O texto indica cerca de 4000 a.C. para início da sedentarização.",
                "Resposta correta: 4000 a.C.",
            ),
            _mc(
                "A camada fértil deixada pelas cheias do Nilo chama-se:",
                ["Delta", "Húmus", "Nomarca", "Insígnia"],
                1,
                "Húmus = sedimento escuro e fértil — «terra negra».",
                "Resposta correta: húmus.",
            ),
            _mc(
                "Quem unificou Alto e Baixo Egito por volta de 3200 a.C.?",
                ["Eça de Queirós", "Menés", "Zahi Hawass", "Gloria Fuertes"],
                1,
                "Menés (ou Narmer) — primeiro faraó da dinastia unificada.",
                "Resposta correta: Menés.",
            ),
            _mc(
                "Durante a cheia do Nilo (julho a outubro), o rio:",
                ["Seca completamente", "Transborda suas margens", "Congela", "Muda de direção para o deserto"],
                1,
                "Cheia = transbordamento; vazante = retorno ao leito normal.",
                "Resposta correta: transborda suas margens.",
            ),
            _mc(
                "Os conjuntos de aldeias no Egito antigo organizavam-se em:",
                ["Estados brasileiros", "Nomos", "Colônias portuguesas", "Massas de ar"],
                1,
                "Nomos ≈ 42 unidades administrativas com nomarcas.",
                "Resposta correta: nomos.",
            ),
            _mc(
                "«Sem o Nilo, o Egito seria a continuação do deserto» porque:",
                ["O Nilo é salgado", "O Nilo traz água e fertilidade à região árida", "O deserto é mais fértil", "Não havia faraós"],
                1,
                "O rio permite vida e agricultura em meio ao deserto.",
                "Resposta correta: o Nilo traz água e fertilidade.",
            ),
            _sa(
                "Cite uma fonte histórica usada para estudar o Egito antigo mencionada no módulo.",
                ["múmia", "mumia", "pintura", "miniatura", "túmulo"],
                "Múmias, pinturas de túmulos e miniaturas são fontes arqueológicas citadas.",
                "Resposta esperada: múmias (ou pinturas de túmulos / miniaturas).",
            ),
            _mc(
                "O Delta do Nilo tem forma:",
                ["Circular", "Triangular (letra Δ)", "Quadrada", "Paralela"],
                1,
                "Delta = forma triangular na desembocadura — nome da letra grega.",
                "Resposta correta: triangular (letra Δ).",
            ),
        ],
    }


def build_simulado() -> dict:
    return {
        "title": "Simulado da PI",
        "icon": "★",
        "intro": """Um teste com <strong>24 questões</strong> (3 por disciplina), todas de múltipla escolha,
              ligadas ao texto abaixo sobre o <strong>Projeto Água e Memória</strong> e ao conteúdo das abas.""",
        "textTitle": "Texto-base — Projeto Água e Memória na Escola",
        "text": """
            <p>No <strong>2º trimestre</strong>, a escola lançou o projeto «Água e Memória». Na feira de Ciências,
            um infográfico mostrou que <strong>96,5%</strong> da água do planeta é salgada e que a maior parte
            da água doce está em <strong>glaciares</strong>. Um grupo explicou a <strong>poluição térmica</strong>:
            quando fábricas despejam água aquecida nos rios, o <strong>oxigênio dissolvido</strong> diminui.</p>

            <p>Em História, uma maquete do <strong>Vale do Nilo</strong> ilustrou a <strong>cheia</strong>
            (julho a outubro) e a <strong>vazante</strong>, quando o rio deixa <strong>húmus</strong> — a «terra negra»
            que permitiu a agricultura egípcia por volta de <strong>4000 a.C.</strong> Um cartaz citava
            <strong>Menés</strong>, que unificou o Egito em <strong>3200 a.C.</strong></p>

            <p>Na aula de Geografia, compararam o clima tropical do Norte com o Sul mais temperado.
            Falaram da <strong>massa Polar Atlântica (mPa)</strong>, que no inverno provoca <strong>friagem</strong>
            na Amazônia e <strong>geadas</strong> no Sul. Macapá tem temperatura média de <strong>27 °C</strong>;
            Florianópolis, <strong>20 °C</strong>.</p>

            <p>Em Português, os alunos reescreveram um parágrafo usando <strong>conectores</strong>
            (<em>porque, mas, por isso</em>) e revisaram oxítonas como <em>café</em> e <em>baú</em>.
            O cartaz da feira (só imagens e números) foi classificado como texto <strong>não verbal</strong>.</p>

            <p>Para calcular materiais, Matemática montou expressões: se a escola recebe
            <strong>52 livros</strong>, destina <strong>15</strong> para cada uma das <strong>duas</strong> turmas
            do 6º ano e o restante vai à biblioteca, sobram <strong>22 livros</strong>
            (<em>52 − 2 × 15 = 22</em>). Outro grupo resolveu <em>50 − 2 × 16 = 18</em> reais de troco numa compra.</p>

            <p>Desenho Geométrico desenhou a fachada do estande com <strong>retas paralelas e perpendiculares</strong>.
            Inglês registrou: «We <strong>were preparing</strong> the posters when the teacher <strong>arrived</strong>».
            Espanhol colou receitas: «A los niños <strong>les gusta</strong> la sopa; a mí <strong>me gustan</strong>
            las ensaladas» — tema do Módulo 8 sobre alimentação e fome.</p>""",
        "questions": [
            {
                "discipline": "Inglês",
                "question": "No texto: «We were preparing the posters when the teacher arrived.» Qual ação estava em progresso?",
                "options": ["The teacher arrived", "We were preparing the posters", "Both in simple past", "Neither"],
                "correctAnswer": 1,
                "explanation": "Past Progressive (were preparing) = ação em andamento; arrived = interrupção.",
            },
            {
                "discipline": "Inglês",
                "question": "Qual conector liga a ação em progresso à interrupção na frase do projeto?",
                "options": ["while", "when", "because", "before"],
                "correctAnswer": 1,
                "explanation": "When aparece antes de arrived (Simple Past).",
            },
            {
                "discipline": "Inglês",
                "question": "Complete: «They ___ soccer when a dog took their ball.»",
                "options": ["were playing", "played", "are playing", "were play"],
                "correctAnswer": 0,
                "explanation": "Ação em progresso → were + -ing.",
            },
            {
                "discipline": "Geografia",
                "question": "Segundo o texto, Macapá (27 °C) é mais quente que Florianópolis (20 °C) principalmente por:",
                "options": ["Estar mais ao sul", "Estar mais próxima do Equador (menor latitude)", "Receber só mPa", "Ter maior altitude"],
                "correctAnswer": 1,
                "explanation": "Macapá fica no Norte, mais perto do Equador → maior temperatura média.",
            },
            {
                "discipline": "Geografia",
                "question": "A mPa no inverno pode causar friagem na Amazônia. Essa massa é:",
                "options": ["Quente e úmida", "Fria e seca", "Quente e seca", "Equatorial continental"],
                "correctAnswer": 1,
                "explanation": "mPa = Polar Atlântica — fria e seca na origem.",
            },
            {
                "discipline": "Geografia",
                "question": "A maior parte do Brasil está na zona climática:",
                "options": ["Polar", "Temperada", "Tropical", "Glacial"],
                "correctAnswer": 2,
                "explanation": "Brasil está majoritariamente entre os trópicos.",
            },
            {
                "discipline": "Matemática",
                "question": "52 livros: 15 para cada uma das 2 turmas. Quantos vão à biblioteca?",
                "options": ["30", "22", "37", "15"],
                "correctAnswer": 1,
                "explanation": "52 − 2 × 15 = 52 − 30 = 22.",
            },
            {
                "discipline": "Matemática",
                "question": "Qual é o valor de 50 − 2 × 16?",
                "options": ["768", "18", "32", "48"],
                "correctAnswer": 1,
                "explanation": "2 × 16 = 32; 50 − 32 = 18.",
            },
            {
                "discipline": "Matemática",
                "question": "Calcule: 16 + 2³",
                "options": ["24", "18", "64", "8"],
                "correctAnswer": 0,
                "explanation": "2³ = 8; 16 + 8 = 24.",
            },
            {
                "discipline": "Desenho Geométrico",
                "question": "Na fachada do estande, lados opostos de um retângulo são:",
                "options": ["Perpendiculares", "Paralelos", "Curvos", "Coincidentes"],
                "correctAnswer": 1,
                "explanation": "Lados opostos de retângulos são paralelos.",
            },
            {
                "discipline": "Desenho Geométrico",
                "question": "Retas que se cruzam formando 90° são:",
                "options": ["Paralelas", "Perpendiculares", "Coincidentes", "Secantes obliquas"],
                "correctAnswer": 1,
                "explanation": "Perpendiculares = concorrentes com ângulo reto.",
            },
            {
                "discipline": "Desenho Geométrico",
                "question": "O símbolo // indica retas:",
                "options": ["Perpendiculares", "Paralelas", "Iguais", "Diagonais"],
                "correctAnswer": 1,
                "explanation": "// = paralelas.",
            },
            {
                "discipline": "Ciências",
                "question": "Segundo o infográfico citado, qual porcentagem da água do planeta é salgada?",
                "options": ["3,5%", "50%", "96,5%", "68,7%"],
                "correctAnswer": 2,
                "explanation": "96,5% nos oceanos.",
            },
            {
                "discipline": "Ciências",
                "question": "Poluição térmica reduz principalmente:",
                "options": ["Salinidade", "Oxigênio dissolvido", "Volume dos rios", "Número de peixes sem efeito"],
                "correctAnswer": 1,
                "explanation": "Água quente dissolve menos oxigênio.",
            },
            {
                "discipline": "Ciências",
                "question": "A maior parte da água doce está em:",
                "options": ["Rios", "Glaciares", "Banheiros", "Garrafas"],
                "correctAnswer": 1,
                "explanation": "68,7% da água doce em glaciares.",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "O cartaz só com imagens e números é texto:",
                "options": ["Verbal", "Não verbal", "Epistolar", "Dramático"],
                "correctAnswer": 1,
                "explanation": "Predomínio de imagens/gráficos → não verbal.",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "«Café» leva acento por ser oxítona terminada em:",
                "options": ["-a", "-é", "-o", "-u"],
                "correctAnswer": 1,
                "explanation": "Oxítona em -é (vogal aberta tônica).",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "O conector «porque» indica relação de:",
                "options": ["Oposição", "Causa", "Tempo", "Adição"],
                "correctAnswer": 1,
                "explanation": "Porque = causa/explicação.",
            },
            {
                "discipline": "Espanhol",
                "question": "«A los niños les gusta la sopa» — «les» refere-se a:",
                "options": ["A mí", "Los niños", "La sopa", "Las ensaladas"],
                "correctAnswer": 1,
                "explanation": "Les = a eles (los niños).",
            },
            {
                "discipline": "Espanhol",
                "question": "«A mí me gustan las ensaladas» — «gustan» está no plural porque:",
                "options": ["Mí é plural", "Las ensaladas é plural", "Me é plural", "Gustar não varia"],
                "correctAnswer": 1,
                "explanation": "Com gustar, o verbo concorda com a coisa gostada (ensaladas = plural).",
            },
            {
                "discipline": "Espanhol",
                "question": "O Módulo 8 aborda alimentação e também:",
                "options": ["Vulcões", "Fome como problema social", "Copa do Mundo", "Placas tectônicas"],
                "correctAnswer": 1,
                "explanation": "Textos sobre fome, villa miseria e direito à alimentação.",
            },
            {
                "discipline": "História",
                "question": "A «terra negra» egípcia formava-se com:",
                "options": ["Areia do deserto", "Húmus das cheias do Nilo", "Neve", "Lava vulcânica"],
                "correctAnswer": 1,
                "explanation": "Cheia depositava húmus fértil.",
            },
            {
                "discipline": "História",
                "question": "Menés unificou o Egito por volta de:",
                "options": ["4000 a.C.", "3200 a.C.", "1500 d.C.", "1937"],
                "correctAnswer": 1,
                "explanation": "3200 a.C. = unificação Alto + Baixo Egito.",
            },
            {
                "discipline": "História",
                "question": "Durante a cheia do Nilo (julho a outubro), o rio:",
                "options": ["Seca", "Transborda", "Congela", "Desvia para o mar Vermelho"],
                "correctAnswer": 1,
                "explanation": "Cheia = transbordamento das margens.",
            },
        ],
    }
