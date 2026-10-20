"""Conteúdo pedagógico da revisão PI — Benjamin, 4º ano (5 disciplinas + simulado)."""

from __future__ import annotations

REVIEW_ID = "benjamin-pi-4ano"
STUDENT_NAME = "Benjamin"
GRADE = "4º ano"
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
        "portugues": _subject_portugues(),
        "historia": _subject_historia(),
        "geografia": _subject_geografia(),
        "ciencias": _subject_ciencias(),
        "matematica": _subject_matematica(),
    }


def _subject_portugues() -> dict:
    return {
        "title": "Língua Portuguesa",
        "icon": "PT",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 7 — O direito de reclamar</strong>: carta de reclamação, e-mail formal,
            tempos verbais do indicativo, locuções verbais e concordância verbal.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Carta de reclamação</h3>
            <p>É um texto em que alguém <strong>reclama</strong> de um produto ou serviço com defeito ou
            que não cumpriu o prometido. Pode ser publicada em sites como o ReclameAQUI ou enviada por e-mail.</p>
            <ul>
              <li>Apresente <strong>quem</strong> reclama, <strong>o quê</strong> aconteceu, <strong>quando</strong> e <strong>onde</strong>.</li>
              <li>Descreva o problema com clareza (ex.: boneca com cabelo repicado).</li>
              <li>Peça uma solução: troca, conserto ou devolução do dinheiro.</li>
            </ul>

            <h3>2. E-mail formal</h3>
            <p>Assunto objetivo · saudação · corpo organizado · despedida · assinatura com nome completo.</p>

            <h3>3. Tempos verbais do indicativo</h3>
            <p>O modo indicativo mostra fatos <strong>certos</strong> no passado, presente ou futuro:</p>
            <ul>
              <li><span class="hl">Pretérito</span> — já aconteceu: <em>A mãe comprou uma boneca.</em></li>
              <li><span class="hl">Presente</span> — acontece agora ou é habitual: <em>Eles jogam bola.</em></li>
              <li><span class="hl">Futuro</span> — vai acontecer: <em>Eu vou reclamar amanhã.</em></li>
            </ul>

            <h3>4. Locuções verbais</h3>
            <p>Dois verbos juntos indicam tempo e ação: <em>está jogando</em> (presente), <em>estava jogando</em> (passado),
            <em>vai jogar</em> ou <em>estará jogando</em> (futuro).</p>

            <h3>5. Concordância verbal</h3>
            <p>O verbo concorda com o <strong>sujeito</strong> em número e pessoa:</p>
            <ul>
              <li><em>A mãe comprou</em> → <em>As mães compraram</em></li>
              <li><em>Eu comprei</em> · <em>Nós compramos</em></li>
            </ul>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Na carta de reclamação, o problema geralmente está no <strong>passado</strong>, mas a pergunta
              «E aí, o que vão fazer?» aponta para uma ação <strong>futura</strong> da empresa.
            </div>""",
            "resumo": """
            <h3>Gêneros — Módulo 7</h3>
            <table>
              <thead><tr><th>Gênero</th><th>Função</th><th>Partes principais</th></tr></thead>
              <tbody>
                <tr><td>Carta de reclamação</td><td>Reclamar de produto/serviço</td><td>Fato · problema · pedido de solução</td></tr>
                <tr><td>E-mail formal</td><td>Comunicação organizada</td><td>Assunto · corpo · despedida · assinatura</td></tr>
              </tbody>
            </table>

            <h3>Tempos do indicativo</h3>
            <table>
              <thead><tr><th>Tempo</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>Pretérito</td><td>O cabelo <span class="hl">caiu</span> e ela <span class="hl">veio</span> descobrir o defeito.</td></tr>
                <tr><td>Presente</td><td>O cabelo <span class="hl">cai</span> e ela <span class="hl">vê</span> o defeito.</td></tr>
                <tr><td>Futuro</td><td>O cabelo <span class="hl">cairá</span> e ela <span class="hl">virá</span> a descobrir.</td></tr>
              </tbody>
            </table>

            <h3>Concordância verbal</h3>
            <p>Verbo muda conforme o sujeito: singular/plural e 1ª, 2ª ou 3ª pessoa.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              «Consolidada» = firme, respeitada · «Inadmissível» = inaceitável.
            </div>""",
            "dicas": """
            <ul>
              <li>Leia o enunciado inteiro antes de marcar tempo verbal ou concordância.</li>
              <li>Identifique o <strong>sujeito</strong> antes de escolher a forma do verbo.</li>
              <li>Em carta de reclamação, separe o que já aconteceu (passado) do que se espera (futuro).</li>
              <li>Em e-mail, o assunto deve resumir o problema em poucas palavras.</li>
              <li>Locuções verbais têm verbo auxiliar + verbo principal: observe os dois.</li>
              <li>Releia a frase substituindo o sujeito por «ele/ela/eles» para testar a concordância.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Na carta publicada no ReclameAQUI, qual é o principal problema relatado?",
                [
                    "A loja fechou antes do horário",
                    "A boneca tinha o cabelo repicado sob o chapéu",
                    "A menina não gostou da cor da boneca",
                    "O site não aceitou a reclamação",
                ],
                1,
                "A mãe comprou a boneca e, ao tirar o chapéu, viu o cabelo totalmente repicado.",
                "Resposta correta: a boneca tinha o cabelo repicado sob o chapéu.",
            ),
            _mc(
                "O que significa «inadmissível» no contexto da carta?",
                ["Muito caro", "Inaceitável", "Consolidado", "Repicado"],
                1,
                "Inadmissível = inaceitável — o defeito não deveria existir em um produto novo.",
                "Resposta correta: inaceitável.",
            ),
            _mc(
                "«No meio do caminho, o chapeuzinho caiu.» — Qual tempo verbal está sublinhado?",
                ["Presente", "Pretérito perfeito", "Futuro", "Infinitivo"],
                1,
                "«Caiu» indica ação concluída no passado — pretérito perfeito do indicativo.",
                "Resposta correta: pretérito perfeito.",
            ),
            _mc(
                "Reescreva mentalmente no presente: «A mãe comprou uma boneca.» Fica:",
                ["A mãe comprará uma boneca.", "A mãe compra uma boneca.", "A mãe compraram uma boneca.", "A mãe comprava uma boneca."],
                1,
                "No presente, o verbo concorda com «A mãe» (3ª pessoa do singular): compra.",
                "Resposta correta: A mãe compra uma boneca.",
            ),
            _mc(
                "«E aí, o que vão fazer?» — O tempo verbal indica:",
                ["Passado", "Presente", "Futuro", "Imperativo"],
                2,
                "A pergunta espera uma ação que a empresa ainda realizará — futuro do indicativo.",
                "Resposta correta: futuro.",
            ),
            _mc(
                "Qual frase está com concordância verbal correta?",
                ["As mães compra bonecas.", "A mãe compraram boneca.", "As mães compraram bonecas.", "Eu compramos boneca."],
                2,
                "Sujeito plural «As mães» exige verbo no plural: compraram.",
                "Resposta correta: As mães compraram bonecas.",
            ),
            _sa(
                "Cite duas informações que não podem faltar numa carta de reclamação.",
                ["problema", "produto", "quando", "onde", "solução", "defeito"],
                "A carta deve deixar claro o que foi comprado, o defeito e o que se espera como solução.",
                "Resposta esperada: descrição do problema/defeito e pedido de solução (troca, conserto ou reembolso). "
                "Também vale mencionar data, local da compra ou identificação do produto.",
            ),
            _mc(
                "Qual opção é uma locução verbal no presente?",
                ["jogou bola", "está jogando bola", "jogará bola", "jogava bola"],
                1,
                "«Está jogando» = auxiliar no presente + gerúndio — locução verbal.",
                "Resposta correta: está jogando bola.",
            ),
        ],
    }


def _subject_historia() -> dict:
    return {
        "title": "História",
        "icon": "HI",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do <strong>Módulo 6 — A conquista de territórios</strong>: Grandes Navegações,
            instrumentos de navegação, rotas marítimas e conquistas portuguesas (Ceuta, Índia, Brasil).</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Grandes Navegações</h3>
            <p>No século XV, europeus — especialmente portugueses — passaram a navegar longas distâncias
            pelo Atlântico e Índico em busca de <strong>rotas comerciais</strong>, especiarias e territórios.</p>

            <h3>2. Instrumentos de navegação</h3>
            <ul>
              <li><span class="hl">Bússola</span> — indica o Norte com agulha magnetizada e rosa dos ventos.</li>
              <li><span class="hl">Astrolábio</span> — mede a altura do Sol ao meio-dia para calcular posição.</li>
              <li><span class="hl">Quadrante</span> — ajuda a medir a altura da Estrela Polar.</li>
            </ul>
            <p>Antes de embarcar, navegantes estudavam mapas antigos e aprimoravam esses instrumentos.</p>

            <h3>3. Caravelas</h3>
            <p>Navios ágeis, com velas triangulares, usados nas viagens de descoberta e comércio.</p>

            <h3>4. Marcos das navegações portuguesas</h3>
            <ul>
              <li><strong>1415</strong> — conquista de <span class="hl">Ceuta</span> (início da expansão marítima).</li>
              <li><strong>1498</strong> — <span class="hl">Vasco da Gama</span> chega às Índias contornando a África.</li>
              <li><strong>1500</strong> — <span class="hl">Pedro Álvares Cabral</span> chega ao Brasil.</li>
            </ul>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Perigos <em>reais</em> no mar: tempestades, falta de alimento. Perigos <em>imaginários</em> nos mapas antigos:
              monstros marinhos desenhados por desconhecimento.
            </div>""",
            "resumo": """
            <h3>Grandes Navegações — síntese</h3>
            <table>
              <thead><tr><th>Conceito</th><th>Ideia-chave</th></tr></thead>
              <tbody>
                <tr><td>Objetivo</td><td>Novas rotas comerciais · especiarias · territórios</td></tr>
                <tr><td>Navio</td><td>Caravela — velas triangulares · ágil</td></tr>
                <tr><td>Bússola</td><td>Localizar o Norte · rosa dos ventos</td></tr>
                <tr><td>Astrolábio / Quadrante</td><td>Medir posição pelo Sol ou Estrela Polar</td></tr>
              </tbody>
            </table>

            <h3>Datas importantes</h3>
            <table>
              <thead><tr><th>Ano</th><th>Evento</th></tr></thead>
              <tbody>
                <tr><td>1415</td><td>Conquista de Ceuta</td></tr>
                <tr><td>1498</td><td>Vasco da Gama chega à Índia</td></tr>
                <tr><td>1500</td><td>Cabral chega ao Brasil</td></tr>
              </tbody>
            </table>""",
            "dicas": """
            <ul>
              <li>Associe cada instrumento à função: bússola = direção · astrolábio/quadrante = posição.</li>
              <li>Não confunda Vasco da Gama (Índia, 1498) com Cabral (Brasil, 1500).</li>
              <li>Em questões com imagem de mapa antigo, monstros marinhos são medo do desconhecido, não fatos.</li>
              <li>Ceuta (1415) marca o início da expansão marítima portuguesa.</li>
              <li>Caravelas permitiam voltar contra o vento — essencial nas longas viagens.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "O que foram as Grandes Navegações?",
                [
                    "Guerras apenas dentro da Europa",
                    "Expedições marítimas europeias em busca de rotas e comércio",
                    "Viagens feitas só por navios a vapor",
                    "Rotas terrestres pela Ásia",
                ],
                1,
                "Grandes Navegações = viagens marítimas de longa distância, especialmente a partir do século XV.",
                "Resposta correta: expedições marítimas europeias em busca de rotas e comércio.",
            ),
            _mc(
                "Qual instrumento indica a direção do Norte?",
                ["Astrolábio", "Quadrante", "Bússola", "Telescópio"],
                2,
                "A bússola usa agulha magnetizada apontando para o Norte.",
                "Resposta correta: bússola.",
            ),
            _mc(
                "Em que ano os portugueses conquistaram Ceuta?",
                ["1500", "1415", "1498", "1320"],
                1,
                "Ceuta foi conquistada em 1415, marco inicial da expansão portuguesa.",
                "Resposta correta: 1415.",
            ),
            _mc(
                "Quem chegou ao Brasil em 1500?",
                ["Vasco da Gama", "Cristóvão Colombo", "Pedro Álvares Cabral", "Fernão de Magalhães"],
                2,
                "Pedro Álvares Cabral comandou a expedição que chegou ao território brasileiro em 1500.",
                "Resposta correta: Pedro Álvares Cabral.",
            ),
            _mc(
                "Vasco da Gama é associado principalmente a:",
                ["A conquista de Ceuta", "A chegada às Índias contornando a África", "A descoberta do Brasil", "A invenção da bússola"],
                1,
                "Em 1498, Vasco da Gama alcançou as Índias pelo cabo da Boa Esperança.",
                "Resposta correta: a chegada às Índias contornando a África.",
            ),
            _sa(
                "Cite um perigo real e um perigo imaginário que aparecem em mapas antigos de navegação.",
                ["tempestade", "monstro", "fome", "mar", "imaginário", "real"],
                "Perigos reais: tempestades, falta de comida. Imaginários: monstros marinhos desenhados por medo/desconhecimento.",
                "Resposta esperada: perigo real — tempestade ou falta de provisões; imaginário — monstros marinhos.",
            ),
            _mc(
                "Para que servia o astrolábio?",
                ["Medir a temperatura do mar", "Calcular posição pela altura do Sol", "Medir a profundidade", "Prever terremotos"],
                1,
                "O astrolábio media a altura do Sol ao meio-dia para estimar a posição do navio.",
                "Resposta correta: calcular posição pela altura do Sol.",
            ),
            _mc(
                "Qual navio é símbolo das Grandes Navegações portuguesas?",
                ["Transatlântico", "Caravela", "Barca a remo", "Submarino"],
                1,
                "As caravelas eram navios ágeis usados nas viagens de descoberta.",
                "Resposta correta: caravela.",
            ),
        ],
    }


def _subject_geografia() -> dict:
    return {
        "title": "Geografia",
        "icon": "GE",
        "sections": {
            "percurso": f"""
            <p>Conteúdo dos <strong>Módulos 7 e 8</strong>: divisas e conflitos territoriais, cartografia moderna (VANT, satélites),
            IBGE, regiões do Brasil, estados, capitais e necessidades regionais.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Divisas e demarcação</h3>
            <p><span class="hl">Divisa</span> é a linha que separa estados ou municípios. Quando o mapa é impreciso ou antigo,
            podem surgir <strong>conflitos</strong> — moradores e prefeituras discordam sobre a qual estado pertencem.</p>
            <p>A Constituição de 1988 prevê que estados resolvam essas disputas; mapas precisos ajudam nisso.</p>

            <h3>2. Cartografia hoje</h3>
            <p>Tecnologias como <strong>satélites</strong> e <strong>VANTs</strong> (drones) produzem mapas mais rápidos e exatos
            do que desenhos antigos feitos à mão.</p>

            <h3>3. IBGE</h3>
            <p><span class="hl">Instituto Brasileiro de Geografia e Estatística</span> — criado em 1937. Faz censo a cada 10 anos,
            estuda território, população e condições de vida.</p>

            <h3>4. Regiões do Brasil</h3>
            <p>O Brasil tem <strong>5 regiões</strong>: Norte, Nordeste, Centro-Oeste, Sudeste e Sul.</p>
            <ul>
              <li>Maior <strong>área</strong>: Norte</li>
              <li>Maior <strong>população</strong>: Sudeste</li>
            </ul>

            <h3>5. Estados e capitais</h3>
            <p>27 unidades federativas (26 estados + DF). Cada estado tem uma <strong>capital</strong> — sede do governo estadual.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Obras públicas (hospitais, rodovias, escolas) dependem do tamanho da população e das necessidades de cada região.
            </div>""",
            "resumo": """
            <h3>IBGE — dados-chave</h3>
            <table>
              <thead><tr><th>Item</th><th>Informação</th></tr></thead>
              <tbody>
                <tr><td>Sigla</td><td>Instituto Brasileiro de Geografia e Estatística</td></tr>
                <tr><td>Criação</td><td>1937</td></tr>
                <tr><td>Funções</td><td>Censo · estatísticas · estudo do território</td></tr>
              </tbody>
            </table>

            <h3>Regiões brasileiras</h3>
            <table>
              <thead><tr><th>Região</th><th>Destaque</th></tr></thead>
              <tbody>
                <tr><td>Norte</td><td>Maior área</td></tr>
                <tr><td>Sudeste</td><td>Maior população</td></tr>
                <tr><td>Nordeste · Sul · Centro-Oeste</td><td>Necessidades específicas de infraestrutura</td></tr>
              </tbody>
            </table>

            <h3>Capitais (exemplos)</h3>
            <table>
              <thead><tr><th>Estado</th><th>Capital</th></tr></thead>
              <tbody>
                <tr><td>Espírito Santo</td><td>Vitória</td></tr>
                <tr><td>Pará</td><td>Belém</td></tr>
                <tr><td>Maranhão</td><td>São Luís</td></tr>
                <tr><td>Santa Catarina</td><td>Florianópolis</td></tr>
                <tr><td>Goiás</td><td>Goiânia</td></tr>
              </tbody>
            </table>""",
            "dicas": """
            <ul>
              <li>IBGE ≠ «Instituto Brasileiro de Gestão» — leia todas as alternativas.</li>
              <li>Brasil = 5 regiões · 27 UFs (inclui DF).</li>
              <li>Mapa antigo × foto de satélite: diferença = tecnologia e precisão.</li>
              <li>Conflitos de divisas geram problemas para municípios (escolas, hospitais).</li>
              <li>Associe obras públicas às necessidades locais e ao tamanho da população.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "O que significa a sigla IBGE?",
                [
                    "Instituto Brasileiro de Gestão Escolar",
                    "Instituto Brasileiro de Geografia e Estatística",
                    "Instituto Brasileiro de Geologia e Energia",
                    "Instituto Brasileiro de Governo e Educação",
                ],
                1,
                "IBGE = Instituto Brasileiro de Geografia e Estatística.",
                "Resposta correta: Instituto Brasileiro de Geografia e Estatística.",
            ),
            _mc(
                "Quantas regiões formam o Brasil hoje?",
                ["4", "5", "6", "27"],
                1,
                "O Brasil está dividido em 5 grandes regiões.",
                "Resposta correta: 5.",
            ),
            _mc(
                "Qual região tem a maior área territorial?",
                ["Sudeste", "Sul", "Norte", "Nordeste"],
                2,
                "A região Norte possui a maior extensão de território.",
                "Resposta correta: Norte.",
            ),
            _mc(
                "Qual é a capital do Espírito Santo?",
                ["Belém", "Vitória", "Goiânia", "Florianópolis"],
                1,
                "Vitória é a capital do Espírito Santo.",
                "Resposta correta: Vitória.",
            ),
            _mc(
                "Por que mapas imprecisos causam conflitos entre estados?",
                ["Porque mudam a cor da bandeira", "Porque dificultam saber a qual estado pertence cada município", "Porque apagam os rios", "Porque somem as capitais"],
                1,
                "Sem demarcação clara, municípios podem ficar sem apoio do estado correto.",
                "Resposta correta: dificultam saber a qual estado pertence cada município.",
            ),
            _mc(
                "Qual tecnologia ajuda a produzir mapas mais precisos hoje?",
                ["Apenas lápis e papel", "Satélites e VANTs (drones)", "Somente bússolas", "Pinturas rupestres"],
                1,
                "Satélites e drones fotografam o território com alta precisão.",
                "Resposta correta: satélites e VANTs (drones).",
            ),
            _sa(
                "Qual região brasileira concentra a maior população?",
                ["sudeste", "Sudeste"],
                "A região Sudeste concentra o maior número de habitantes.",
                "Resposta esperada: Sudeste.",
            ),
            _mc(
                "O IBGE realiza o censo da população a cada quantos anos?",
                ["5", "10", "15", "20"],
                1,
                "O censo demográfico brasileiro é feito a cada 10 anos.",
                "Resposta correta: 10.",
            ),
        ],
    }


def _subject_ciencias() -> dict:
    return {
        "title": "Ciências",
        "icon": "CI",
        "sections": {
            "percurso": f"""
            <p>Conteúdo dos <strong>Módulos 9 e 10</strong>: cadeias alimentares na horta, predadores e presas,
            decompositores, microrganismos, higiene alimentar e compostagem/lixo orgânico.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Cadeia alimentar</h3>
            <p>Mostra quem come quem. Exemplo na horta:</p>
            <ul>
              <li><span class="hl">Produtores</span> — plantas (tomate, alface, morango).</li>
              <li><span class="hl">Consumidores</span> — lagartas, pulgões, percevejos (herbívoros).</li>
              <li><span class="hl">Predadores</span> — joaninhas (comem pulgões), papa-lagartas (comem lagartas).</li>
              <li><span class="hl">Decompositores</span> — fungos, bactérias e minhocas reciclam matéria orgânica no solo.</li>
            </ul>

            <h3>2. Polinizadores</h3>
            <p>Abelhas visitam flores e ajudam na reprodução das plantas — relação benéfica para ambos.</p>

            <h3>3. Microrganismos patogênicos</h3>
            <p>Alguns fungos, bactérias e vírus causam doenças — são <strong>patogênicos</strong> quando prejudicam a saúde.</p>

            <h3>4. Higienização de hortaliças</h3>
            <ol>
              <li>Retirar partes estragadas</li>
              <li>Lavar em água corrente</li>
              <li>Deixar em solução clorada por 15 minutos (desinfecção)</li>
              <li>Enxaguar em água potável</li>
              <li>Secar com papel-toalha ou ao ar</li>
            </ol>

            <h3>5. Compostagem</h3>
            <p>Restos orgânicos (cascas, folhas) viram adubo com ajuda de decompositores — reduz lixo e nutre a horta.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Limpeza remove sujeira visível; <strong>desinfecção</strong> reduz microrganismos que a limpeza não eliminou.
            </div>""",
            "resumo": """
            <h3>Cadeia alimentar — papéis</h3>
            <table>
              <thead><tr><th>Papel</th><th>Exemplo na horta</th></tr></thead>
              <tbody>
                <tr><td>Produtor</td><td>Tomate, alface, morango</td></tr>
                <tr><td>Herbívoro</td><td>Lagarta, pulgão</td></tr>
                <tr><td>Predador</td><td>Joaninha, papa-lagartas</td></tr>
                <tr><td>Decompositor</td><td>Minhoca, fungos, bactérias</td></tr>
              </tbody>
            </table>

            <h3>Higienização — 5 passos</h3>
            <p>Retirar estragados → lavar → cloro 15 min → enxaguar → secar</p>

            <h3>Vocabulário</h3>
            <ul>
              <li><strong>Patogênico</strong> — causa doença</li>
              <li><strong>Desinfecção</strong> — elimina microrganismos restantes</li>
              <li><strong>Compostagem</strong> — reciclar restos orgânicos em adubo</li>
            </ul>""",
            "dicas": """
            <ul>
              <li>Produtor sempre é ser vivo que faz fotossíntese (plantas, algas).</li>
              <li>Decompositores fecham a cadeia — sem eles, restos acumulam no solo.</li>
              <li>Joaninha é predadora de pulgão — não confunda com herbívoro.</li>
              <li>Higienização ≠ só lavar: desinfecção com cloro é etapa extra.</li>
              <li>Compostagem liga lixo orgânico à saúde da horta.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Na horta, quem são os produtores?",
                ["Lagartas", "Plantas como tomate e alface", "Papa-lagartas", "Minhocas"],
                1,
                "Produtores produzem alimento por fotossíntese — as plantas da horta.",
                "Resposta correta: plantas como tomate e alface.",
            ),
            _mc(
                "A joaninha na folha de alface é:",
                ["Produtora", "Herbívora", "Predadora de pulgões", "Decompositora"],
                2,
                "Joaninhas comem pulgões — são predadoras.",
                "Resposta correta: predadora de pulgões.",
            ),
            _mc(
                "Qual ser vivo decompõe restos orgânicos no solo?",
                ["Abelha", "Minhoca", "Percevejo", "Tomate"],
                1,
                "Minhocas, fungos e bactérias decompõem matéria orgânica.",
                "Resposta correta: minhoca.",
            ),
            _mc(
                "O que significa «patogênico»?",
                ["Que ajuda na polinização", "Que pode causar doença", "Que faz fotossíntese", "Que vive só no mar"],
                1,
                "Patogênico = prejudicial à saúde, capaz de causar doença.",
                "Resposta correta: que pode causar doença.",
            ),
            _mc(
                "Quantos minutos as hortaliças devem ficar na solução clorada?",
                ["5", "10", "15", "60"],
                2,
                "O caderno indica imersão na solução clorada por 15 minutos.",
                "Resposta correta: 15.",
            ),
            _sa(
                "Cite dois microrganismos que podem representar risco à saúde nos alimentos.",
                ["bactéria", "bacteria", "vírus", "virus", "fungo", "fungos"],
                "Bactérias, vírus e fungos patogênicos podem contaminar alimentos.",
                "Resposta esperada: bactérias e vírus (ou fungos).",
            ),
            _mc(
                "Para que serve a compostagem?",
                ["Aumentar lixo na lixeira", "Transformar restos orgânicos em adubo", "Eliminar plantas", "Atrair predadores"],
                1,
                "Compostagem recicla restos orgânicos em adubo para a horta.",
                "Resposta correta: transformar restos orgânicos em adubo.",
            ),
            _mc(
                "Qual relação descreve abelha e flor de morango?",
                ["Predação", "Polinização benéfica", "Decomposição", "Competição por solo"],
                1,
                "Abelhas polinizam flores enquanto buscam néctar — relação benéfica.",
                "Resposta correta: polinização benéfica.",
            ),
        ],
    }


def _subject_matematica() -> dict:
    return {
        "title": "Matemática",
        "icon": "MA",
        "sections": {
            "percurso": f"""
            <p>Conteúdo dos <strong>Módulos 17, 19, 20 e 21</strong>: sequências repetitivas e recursivas,
            igualdade e equivalência, multiplicação e quadriláteros.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Sequências repetitivas</h3>
            <p>Têm um <strong>motivo</strong> que se repete: ▲▲● ▲▲● ▲▲●… (dois triângulos e um círculo).</p>

            <h3>2. Sequências recursivas</h3>
            <p>Cada termo segue uma <strong>regra de crescimento</strong>: 0, 2, 4, 6… (+2 a cada passo) ou figuras
            que ganham 1 triângulo por vez.</p>

            <h3>3. Igualdade e equivalência</h3>
            <p>Duas expressões são equivalentes quando têm o <strong>mesmo valor</strong>:</p>
            <ul>
              <li>75 + 35 + 5 = 80 + 35 (somamos 5 aos 75 para chegar a 80)</li>
              <li>87 − 49 ≠ 77 − 49 (lados diferentes após compensação errada)</li>
            </ul>
            <p>Se Ana e Francisco começam com o mesmo dinheiro e terminam iguais, diferenças nas compras se compensam.</p>

            <h3>4. Multiplicação</h3>
            <p>Revisar fatos, decomposição e problemas do caderno (Módulo 20).</p>

            <h3>5. Quadriláteros</h3>
            <p>Polígonos de <strong>4 lados</strong>: quadrado, retângulo, paralelogramo, trapézio, losango.
            Observe lados paralelos e ângulos retos.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Antes de marcar = ou ≠, calcule ou simplifique os dois lados da expressão.
            </div>""",
            "resumo": """
            <h3>Sequências</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Característica</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>Repetitiva</td><td>Motivo que se repete</td><td>▲▲● ▲▲● …</td></tr>
                <tr><td>Recursiva</td><td>Cresce ou diminui por regra fixa</td><td>0, 2, 4, 6… (+2)</td></tr>
              </tbody>
            </table>

            <h3>Igualdade</h3>
            <p>Mesma mudança nos dois lados mantém a igualdade. Calcule antes de comparar.</p>

            <h3>Quadriláteros</h3>
            <table>
              <thead><tr><th>Figura</th><th>Traço principal</th></tr></thead>
              <tbody>
                <tr><td>Quadrado</td><td>4 lados iguais · 4 ângulos retos</td></tr>
                <tr><td>Retângulo</td><td>Lados opostos iguais · 4 ângulos retos</td></tr>
                <tr><td>Paralelogramo</td><td>Lados opostos paralelos</td></tr>
                <tr><td>Trapézio</td><td>Um par de lados paralelos</td></tr>
              </tbody>
            </table>""",
            "dicas": """
            <ul>
              <li>Sequência repetitiva: circule o bloco que volta a aparecer.</li>
              <li>Sequência recursiva: descubra o que muda de um termo ao próximo.</li>
              <li>Em igualdades, faça a conta dos dois lados antes de decidir.</li>
              <li>Problemas de dinheiro: «sobra igual» significa que gastos diferentes se compensam.</li>
              <li>Quadrilátero = 4 lados — conte antes de classificar.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Na sequência ▲▲● ▲▲● ▲▲●, o tipo é:",
                ["Recursiva", "Repetitiva", "Aleatória", "Decrescente"],
                1,
                "O bloco ▲▲● se repete — sequência repetitiva.",
                "Resposta correta: repetitiva.",
            ),
            _mc(
                "Na sequência 0, 2, 4, 6, 8… qual é a regra?",
                ["Multiplicar por 2", "Somar 2 a cada termo", "Subtrair 2", "Repetir 0 e 2"],
                1,
                "Cada termo aumenta 2 unidades — sequência recursiva de crescimento.",
                "Resposta correta: somar 2 a cada termo.",
            ),
            _mc(
                "75 + 35 + 5 = 80 + 35. A igualdade é:",
                ["Verdadeira", "Falsa", "Impossível saber", "Só verdadeira se 5 = 0"],
                0,
                "75 + 5 = 80, então os dois lados valem 115.",
                "Resposta correta: verdadeira.",
            ),
            _mc(
                "87 − 49 = 77 − 49. A igualdade é:",
                ["Verdadeira", "Falsa", "Verdadeira só no domingo", "Verdadeira se 49 = 0"],
                1,
                "87 − 49 = 38, mas 77 − 49 = 28 — valores diferentes.",
                "Resposta correta: falsa.",
            ),
            _mc(
                "Ana Clara gastou R$ 52 em um livro e Francisco R$ 45. Começaram com o mesmo dinheiro e sobraram iguais. O lanche de Francisco:",
                ["Custou R$ 7 a menos que o de Ana", "Custou R$ 7 a mais que o de Ana", "Foi de graça", "Custou o dobro"],
                1,
                "Francisco gastou R$ 7 a menos no livro, então gastou R$ 7 a mais no lanche para sobrar igual.",
                "Resposta correta: custou R$ 7 a mais que o de Ana.",
            ),
            _mc(
                "Thomas tinha R$ 170, gastou R$ 120 na mochila e sobrou R$ 50. Ricardo gastou R$ 80 e também sobrou R$ 50. Ricardo tinha:",
                ["R$ 100", "R$ 120", "R$ 130", "R$ 150"],
                2,
                "Ricardo: valor inicial − 80 = 50 → inicial = 130.",
                "Resposta correta: R$ 130.",
            ),
            _mc(
                "Quantos lados tem um quadrilátero?",
                ["3", "4", "5", "6"],
                1,
                "Quadrilátero = polígono de 4 lados.",
                "Resposta correta: 4.",
            ),
            _sa(
                "Qual figura tem 4 lados iguais e 4 ângulos retos?",
                ["quadrado", "Quadrado"],
                "Quadrado tem 4 lados congruentes e 4 ângulos de 90°.",
                "Resposta esperada: quadrado.",
            ),
        ],
    }


def build_simulado() -> dict:
    return {
        "title": "Simulado da PI",
        "icon": "★",
        "intro": """Um teste com <strong>15 questões</strong> (3 por disciplina), todas de múltipla escolha,
              ligadas ao texto abaixo sobre o projeto «Da horta ao mapa» e ao conteúdo das abas.""",
        "textTitle": "Texto-base — Da horta ao mapa, do lixo ao adubo",
        "text": """
            <p>Na Escola Verde, os alunos do <strong>4º ano</strong> criaram uma <strong>horta comunitária</strong>.
            Plantaram tomates, alfaces e morangos. Para controlar pulgões, observaram <strong>joaninhas</strong>;
            para polinizar as flores, abelhas visitavam os canteiros. Restos de folhas e cascas iam para a
            <strong>compostagem</strong>, onde minhocas e microrganismos transformavam lixo orgânico em adubo.</p>

            <p>Antes de consumir as hortaliças, a merendeira seguia cinco passos de <strong>higienização</strong>,
            incluindo 15 minutos em solução clorada. Quando uma mangueira de irrigação chegou com defeito,
            a professora de Português ajudou a redigir uma <strong>carta de reclamação</strong> ao fornecedor,
            descrevendo a compra feita em março e pedindo troca imediata.</p>

            <p>Em Geografia, o grupo consultou dados do <strong>IBGE</strong> (instituto criado em 1937) e montou
            um mapa das <strong>cinco regiões</strong> do Brasil, destacando que o <strong>Norte</strong> tem a maior
            área e o <strong>Sudeste</strong> concentra a maior população. Colocaram pinos nas capitais:
            <strong>Vitória</strong> (ES), <strong>Belém</strong> (PA) e <strong>Florianópolis</strong> (SC).</p>

            <p>Na feira de História, uma maquete de <strong>caravela</strong> lembrou as Grandes Navegações.
            O cartaz explicava o uso da <strong>bússola</strong> e citava <strong>1415</strong> (Ceuta),
            <strong>1498</strong> (Vasco da Gama na Índia) e <strong>1500</strong> (Cabral no Brasil).</p>

            <p>Para organizar canteiros, os alunos de Matemática montaram <strong>sequências repetitivas</strong>
            de azulejos coloridos e calcularam compras: se dois pacotes de sementes custam R$ 12 cada e
            uma mochila de ferramentas R$ 80, quem começa com R$ 130 e compra só a mochila sobra R$ 50.</p>""",
        "questions": [
            {
                "discipline": "Língua Portuguesa",
                "question": "No texto, a carta de reclamação sobre a mangueira defeituosa provavelmente descreve a compra em qual tempo verbal?",
                "options": ["Futuro", "Pretérito (passado)", "Infinitivo", "Imperativo"],
                "correctAnswer": 1,
                "explanation": "O defeito e a compra em março já aconteceram — usa-se pretérito na descrição do fato.",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "A pergunta «o que vão fazer?» no final de uma reclamação indica expectativa de ação:",
                "options": ["No passado remoto", "No futuro", "No imperativo negativo", "No infinitivo pessoal"],
                "correctAnswer": 1,
                "explanation": "«Vão fazer» aponta para uma ação que a empresa ainda deve realizar.",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "«As professoras organizaram a feira.» — Se o sujeito fosse «A professora», o verbo ficaria:",
                "options": ["organizaram", "organiza", "organizou", "organizamos"],
                "correctAnswer": 2,
                "explanation": "Sujeito singular exige «organizou» no pretérito.",
            },
            {
                "discipline": "História",
                "question": "Segundo o cartaz da feira, em 1498 Vasco da Gama:",
                "options": ["Chegou ao Brasil", "Conquistou Ceuta", "Chegou às Índias", "Inventou a bússola"],
                "correctAnswer": 2,
                "explanation": "1498 marca a chegada de Vasco da Gama às Índias.",
            },
            {
                "discipline": "História",
                "question": "O instrumento citado no texto para indicar o Norte durante as navegações é:",
                "options": ["Astrolábio", "Quadrante", "Bússola", "Telescópio"],
                "correctAnswer": 2,
                "explanation": "O texto menciona explicitamente a bússola na maquete.",
            },
            {
                "discipline": "História",
                "question": "A conquista de Ceuta, associada ao início da expansão portuguesa, ocorreu em:",
                "options": ["1500", "1415", "1937", "1498"],
                "correctAnswer": 1,
                "explanation": "1415 = conquista de Ceuta, citada no cartaz.",
            },
            {
                "discipline": "Geografia",
                "question": "De acordo com o texto, o IBGE foi criado em:",
                "options": ["1988", "1937", "1500", "1415"],
                "correctAnswer": 1,
                "explanation": "O texto informa que o IBGE foi criado em 1937.",
            },
            {
                "discipline": "Geografia",
                "question": "Qual região brasileira tem a maior área, segundo o mapa montado pelos alunos?",
                "options": ["Sudeste", "Sul", "Norte", "Centro-Oeste"],
                "correctAnswer": 2,
                "explanation": "O texto destaca o Norte como região de maior área.",
            },
            {
                "discipline": "Geografia",
                "question": "Florianópolis é capital de qual estado mencionado no mapa?",
                "options": ["Espírito Santo", "Pará", "Santa Catarina", "Goiás"],
                "correctAnswer": 2,
                "explanation": "Florianópolis é a capital de Santa Catarina.",
            },
            {
                "discipline": "Ciências",
                "question": "As joaninhas na horta da Escola Verde ajudam controlando:",
                "options": ["Pulgões", "Minhocas", "Tomates", "Abelhas"],
                "correctAnswer": 0,
                "explanation": "Joaninhas são predadoras de pulgões, citadas no texto.",
            },
            {
                "discipline": "Ciências",
                "question": "Na compostagem descrita, quem transforma restos orgânicos em adubo?",
                "options": ["Apenas abelhas", "Minhocas e microrganismos", "Papa-lagartas", "Estudantes com cloro"],
                "correctAnswer": 1,
                "explanation": "Minhocas e microrganismos decompõem matéria orgânica na compostagem.",
            },
            {
                "discipline": "Ciências",
                "question": "Quantos minutos as hortaliças ficam na solução clorada, segundo a merendeira?",
                "options": ["5", "10", "15", "30"],
                "correctAnswer": 2,
                "explanation": "O texto cita 15 minutos de imersão em solução clorada.",
            },
            {
                "discipline": "Matemática",
                "question": "Dois pacotes de sementes a R$ 12 cada custam no total:",
                "options": ["R$ 12", "R$ 14", "R$ 24", "R$ 36"],
                "correctAnswer": 2,
                "explanation": "2 × 12 = 24 reais.",
            },
            {
                "discipline": "Matemática",
                "question": "Quem começa com R$ 130, gasta R$ 80 na mochila e sobra:",
                "options": ["R$ 40", "R$ 50", "R$ 60", "R$ 210"],
                "correctAnswer": 1,
                "explanation": "130 − 80 = 50 reais de troco.",
            },
            {
                "discipline": "Matemática",
                "question": "Os azulejos coloridos organizados em blocos que se repetem formam sequência:",
                "options": ["Recursiva de subtração", "Repetitiva", "Aleatória sem padrão", "Só numérica"],
                "correctAnswer": 1,
                "explanation": "Quando um bloco inteiro se repete, trata-se de sequência repetitiva.",
            },
        ],
    }
