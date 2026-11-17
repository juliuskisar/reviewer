"""Conteúdo pedagógico da revisão PI 3º trimestre — Benjamin, 4º ano (5 disciplinas + simulado)."""

from __future__ import annotations

REVIEW_ID = "benjamin-pi-4ano-3tri"
STUDENT_NAME = "Benjamin"
GRADE = "4º ano"
PAGE_TITLE = f"Revisão Multidisciplinar PI 3º Trimestre — {STUDENT_NAME} ({GRADE})"

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
            <p>Conteúdo dos <strong>Módulos 9, 10, 11 e 13</strong>: peça «Viravez, o cortês», discurso direto e indireto,
            telejornal sobre Tarsila do Amaral, pronomes, texto instrucional e histórias fantásticas (mitos e lendas).</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Texto teatral — «Viravez, o cortês»</h3>
            <p>A peça é feita de <strong>falas</strong> (com o nome do personagem antes) e <strong>rubricas</strong>
            (indicações de cena). <span class="hl">Viravez</span> é o protagonista: ele solta o Saci, que o recompensa
            com muita comida — desde que guarde segredo. Inácia, a esposa, desconfia da fartura, e Viravez inventa
            a «herança do tio Hipólito».</p>
            <ul>
              <li><strong>Rubrica de cena</strong> — movimento ou gesto: <em>Vivaldino se inclina e beija a mão de Inácia.</em></li>
              <li><strong>Rubrica de fala</strong> — tom de voz: <em>(descrente)</em>, <em>(em tom brincalhão)</em>.</li>
            </ul>

            <h3>2. Discurso direto e indireto</h3>
            <ul>
              <li><span class="hl">Direto</span> — fala exata, com dois-pontos e travessão: <em>Viravez disse: — É uma herança.</em></li>
              <li><span class="hl">Indireto</span> — o narrador conta o que foi dito: <em>Viravez disse que era uma herança.</em></li>
            </ul>

            <h3>3. Telejornal e Tarsila do Amaral</h3>
            <p>O telejornal usa <strong>imagem, som, entonação e gestos</strong> — recursos que o jornal impresso não tem.
            A reportagem «Tarsila para Crianças» mostrou obras da pintora, como o <strong>Abaporu</strong> (1928).
            Tarsila usou nas telas as cores «caipiras» de que gostava desde a infância.</p>

            <h3>4. Pronomes</h3>
            <p>Pronomes <strong>evitam repetição</strong> de palavras:</p>
            <ul>
              <li><span class="hl">Pessoais</span> — eu, tu, ele, ela, nós, eles: <em>Os mosquitos? Eles vão embora.</em></li>
              <li><span class="hl">Possessivos</span> — indicam dono: <em>meu quarto</em>, <em>seu pai</em>, <em>suas telas</em>.</li>
              <li><span class="hl">Oblíquos o, a, os, as</span> — substituem o complemento: <em>Maria viu a rosa e <u>a</u> colocou no vaso.</em></li>
            </ul>
            <p>Ortografia: verbos em <strong>-car</strong> no pretérito trocam c por qu antes de e — <em>brinco → brinquei</em>.</p>

            <h3>5. Texto instrucional</h3>
            <p>Ensina <strong>como fazer</strong> algo: título, objetivo, <strong>materiais</strong> e <strong>passo a passo em ordem</strong>.
            No vídeo tutorial, também se planejam a apresentação, a fala, a postura e a despedida.</p>

            <h3>6. Mitos e lendas (Módulo 13)</h3>
            <ul>
              <li><span class="hl">Mito</span> — explica origens do mundo e da natureza com deuses e heróis: Narciso vira flor; Aracne, tecelã, desafia a deusa Atena.</li>
              <li><span class="hl">Lenda</span> — história popular que <strong>mistura fantasia e realidade</strong>: em «A origem da lavoura», a moça desce do céu com a chuva (fantasia), mas a chuva realmente ajuda as plantações (realidade).</li>
            </ul>
            <p>Para não repetir o nome, a narrativa troca «Narciso» por <em>o menino</em>, <em>o jovem</em>, <em>seu filho</em>.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Mitos e lendas foram contados <strong>oralmente</strong>, de geração em geração, antes de serem escritos.
            </div>""",
            "resumo": """
            <h3>Gêneros estudados</h3>
            <table>
              <thead><tr><th>Gênero</th><th>Marca principal</th></tr></thead>
              <tbody>
                <tr><td>Peça teatral</td><td>Falas com nome do personagem · rubricas</td></tr>
                <tr><td>Telejornal</td><td>Imagem · som · voz · ao vivo</td></tr>
                <tr><td>Entrevista</td><td>Roteiro · perguntas abertas · agradecimento</td></tr>
                <tr><td>Texto instrucional</td><td>Objetivo · materiais · passos em ordem</td></tr>
                <tr><td>Mito / lenda</td><td>Seres fantásticos · explica algo da natureza</td></tr>
              </tbody>
            </table>

            <h3>Discurso</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>Direto</td><td>Inácia perguntou: — Onde está o dinheiro?</td></tr>
                <tr><td>Indireto</td><td>Inácia perguntou onde estava o dinheiro.</td></tr>
              </tbody>
            </table>

            <h3>Pronomes</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Exemplos</th></tr></thead>
              <tbody>
                <tr><td>Pessoal</td><td>eu · ele · ela · nós · eles</td></tr>
                <tr><td>Possessivo</td><td>meu · seu · sua · suas</td></tr>
                <tr><td>Oblíquo (objeto)</td><td>o · a · os · as</td></tr>
              </tbody>
            </table>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Lenda = fantasia + realidade. Mito grego = deuses e heróis explicando origens.
            </div>""",
            "dicas": """
            <ul>
              <li>Travessão depois de dois-pontos = discurso direto.</li>
              <li>Para achar a quem o pronome se refere, volte à frase anterior e procure o nome.</li>
              <li>Rubrica fica entre parênteses e não é falada pelo ator.</li>
              <li>Em texto instrucional, a ordem dos passos não pode ser trocada.</li>
              <li>Em lendas, separe o que é fantasioso do que pode acontecer de verdade.</li>
              <li>-car no pretérito: <em>toquei, brinquei, fiquei</em>.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Na peça «Viravez, o cortês», Viravez solta o Saci e recebe muita comida em troca de segredo. "
                "Quem é o protagonista da peça?",
                ["Inácia", "Viravez", "O Saci", "O tio Hipólito"],
                1,
                "Protagonista é o personagem principal — Viravez, que move a história.",
                "Resposta correta: Viravez.",
            ),
            _mc(
                "Qual frase está em discurso direto?",
                [
                    "Viravez contou que era uma herança.",
                    "Inácia perguntou onde estava o dinheiro.",
                    "Viravez disse: — Já falei que é uma herança.",
                    "Inácia desconfiou da fartura.",
                ],
                2,
                "Discurso direto reproduz a fala exata, com dois-pontos e travessão.",
                "Resposta correta: Viravez disse: — Já falei que é uma herança.",
            ),
            _mc(
                "Na peça, aparece a rubrica «INÁCIA (descrente) — Coisa mais esquisita!». A palavra «descrente» indica:",
                ["O tom da fala da personagem", "O nome do cenário", "O título da peça", "A fala do narrador"],
                0,
                "Rubrica de fala mostra como a fala deve ser dita — aqui, com desconfiança.",
                "Resposta correta: o tom da fala da personagem.",
            ),
            _mc(
                "Que recursos a reportagem de telejornal «Tarsila para Crianças» pode usar que o jornal impresso não tem?",
                [
                    "Apenas títulos em letras grandes",
                    "Imagens ao vivo, sons e entonação da voz",
                    "Somente fotos em preto e branco",
                    "Texto escrito sem autor",
                ],
                1,
                "A TV combina imagem, som e voz — recursos audiovisuais.",
                "Resposta correta: imagens ao vivo, sons e entonação da voz.",
            ),
            _mc(
                "«Maria viu a rosa e a colocou no vaso.» A palavra destacada «a» (em «a colocou») substitui:",
                ["Maria", "o vaso", "a rosa", "a mãe"],
                2,
                "O pronome oblíquo «a» retoma «a rosa», evitando repetir a palavra.",
                "Resposta correta: a rosa.",
            ),
            _mc(
                "«Tarsila passou a infância nas fazendas de seu pai.» A palavra «seu» é um pronome:",
                ["Pessoal", "Demonstrativo", "Artigo", "Possessivo"],
                3,
                "«Seu» indica de quem é o pai (de Tarsila) — pronome possessivo.",
                "Resposta correta: possessivo.",
            ),
            _mc(
                "Qual é a forma correta do verbo «brincar» no pretérito, com «eu»?",
                ["Eu brincei", "Eu brinquei", "Eu brinqueu", "Eu brincou"],
                1,
                "Verbos em -car trocam c por qu antes de e: brinquei.",
                "Resposta correta: Eu brinquei.",
            ),
            _mc(
                "Em um texto instrucional (por exemplo, como montar um jogo), a parte «Materiais» serve para:",
                [
                    "Contar o final da história",
                    "Apresentar os personagens",
                    "Dar a opinião do autor",
                    "Listar o que é preciso para fazer a atividade",
                ],
                3,
                "Materiais = lista do que vamos usar; depois vêm os passos em ordem.",
                "Resposta correta: listar o que é preciso para fazer a atividade.",
            ),
            _mc(
                "No mito grego de Narciso, o jovem se encanta com a própria imagem refletida no lago. "
                "No fim da história, ele se transforma em:",
                ["Uma flor", "Um vaga-lume", "Uma serpente", "Uma estrela"],
                0,
                "O mito explica a origem da flor narciso.",
                "Resposta correta: uma flor.",
            ),
            _mc(
                "Na lenda «A origem da lavoura», uma moça desce do céu com a chuva e ensina a plantar. "
                "Qual fato da lenda é fantasioso?",
                [
                    "A chuva ajuda as plantações a crescer",
                    "A moça desce do céu com a chuva",
                    "A terra preparada pode ser plantada",
                    "O beiju é feito com mandioca",
                ],
                1,
                "Lendas misturam fantasia (a moça vinda do céu) e realidade (chuva ajuda a lavoura).",
                "Resposta correta: a moça desce do céu com a chuva.",
            ),
            _sa(
                "Leia a anedota: «— Pai, tem muitos mosquitos no meu quarto! — Apague a luz que eles vão embora!» "
                "A quem se refere o pronome «eles»? E que tipo de pronome é «meu»?",
                ["mosquitos", "possessivo"],
                "«Eles» retoma «mosquitos» (pronome pessoal); «meu» indica posse (possessivo).",
                "Resposta esperada: «eles» = os mosquitos; «meu» é pronome possessivo.",
            ),
        ],
    }


def _subject_historia() -> dict:
    return {
        "title": "História",
        "icon": "HI",
        "sections": {
            "percurso": f"""
            <p>Conteúdo dos <strong>Módulos 8, 9 e 10</strong> e da leitura sobre o <strong>povo Suiá</strong>:
            reinos africanos, tráfico e resistência, engenhos de açúcar, bandeirantes, ouro em Minas
            e técnicas indígenas de conservação de alimentos (polvilho).</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Reinos africanos</h3>
            <p>Os <span class="hl">bantus</span> formaram reinos organizados, com agricultura, comércio e metalurgia.</p>
            <ul>
              <li><strong>Congo</strong> — capital Mbanza Congo; usava conchas chamadas <span class="hl">nzimbu</span> como moeda.</li>
              <li><strong>Ndongo</strong> (atual Angola) — a rainha <span class="hl">Njinga a Mbande</span> resistiu aos portugueses.</li>
            </ul>

            <h3>2. Tráfico e resistência</h3>
            <p>Portugueses construíram fortes no litoral africano para comerciar e, depois, traficar pessoas escravizadas.
            Milhões de africanos foram levados à força em <strong>navios negreiros</strong> — essa dispersão forçada se chama
            <span class="hl">diáspora</span>. Muitos resistiram, fugindo e formando <span class="hl">quilombos</span>.</p>

            <h3>3. Engenhos de açúcar</h3>
            <p>Em <strong>1532</strong>, Martim Afonso de Sousa fundou <strong>São Vicente</strong> (SP); logo surgiram engenhos.
            A cana era moída e o caldo virava açúcar para exportar. Primeiro trabalharam indígenas escravizados; depois,
            cada vez mais africanos escravizados, que trouxeram conhecimentos de <strong>metalurgia</strong>.</p>

            <h3>4. Bandeirantes e ouro</h3>
            <p>As <span class="hl">bandeiras</span> partiam de <strong>São Paulo de Piratininga</strong> rumo ao sertão em busca de
            indígenas, riquezas e ouro. Em Minas Gerais encontrou-se ouro de dois tipos:</p>
            <ul>
              <li><strong>Aluvião</strong> — partículas na areia dos rios (lavadas com bateia).</li>
              <li><strong>Filão</strong> — veio de ouro dentro da rocha.</li>
            </ul>
            <p><strong>Tropeiros</strong> levavam alimentos em mulas até as minas; surgiram vilas como Mariana, Ouro Preto e Sabará.</p>

            <h3>5. O polvilho do povo Suiá</h3>
            <p>Os Suiá, do Xingu, observaram a natureza e criaram uma técnica de <strong>conservação de alimentos</strong>:</p>
            <ul>
              <li>As <strong>mulheres</strong> colhem e ralam a mandioca na <strong>época da seca</strong>, para o polvilho secar ao sol.</li>
              <li>Os <strong>homens</strong> fazem <strong>cestos</strong> para guardar o polvilho seco.</li>
              <li>Guardado assim, o polvilho <strong>dura até um ano</strong> — serve para beiju, mingau e bolos.</li>
            </ul>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              A divisão do trabalho entre homens e mulheres e o calendário da seca e da chuva fazem parte do conhecimento tradicional Suiá.
            </div>""",
            "resumo": """
            <h3>Linha do tempo</h3>
            <table>
              <thead><tr><th>Quando</th><th>O quê</th></tr></thead>
              <tbody>
                <tr><td>Século XV</td><td>Portugueses comerciam no litoral africano</td></tr>
                <tr><td>1532</td><td>Fundação de São Vicente · primeiros engenhos</td></tr>
                <tr><td>Século XVII</td><td>Bandeiras saem de São Paulo</td></tr>
                <tr><td>Séculos XVII–XVIII</td><td>Ouro em Minas · vilas mineradoras</td></tr>
              </tbody>
            </table>

            <h3>Palavras-chave</h3>
            <table>
              <thead><tr><th>Palavra</th><th>Significado</th></tr></thead>
              <tbody>
                <tr><td>Nzimbu</td><td>Conchas usadas como moeda no Congo</td></tr>
                <tr><td>Diáspora</td><td>Dispersão forçada de africanos</td></tr>
                <tr><td>Quilombo</td><td>Refúgio de quem fugia da escravização</td></tr>
                <tr><td>Aluvião / filão</td><td>Ouro no rio / ouro na rocha</td></tr>
                <tr><td>Tropeiro</td><td>Comerciante que levava mercadorias em mulas</td></tr>
              </tbody>
            </table>

            <h3>Polvilho Suiá</h3>
            <table>
              <thead><tr><th>Quem</th><th>Faz o quê</th></tr></thead>
              <tbody>
                <tr><td>Mulheres</td><td>Colhem e ralam a mandioca na seca</td></tr>
                <tr><td>Homens</td><td>Fazem cestos para guardar</td></tr>
                <tr><td>Resultado</td><td>Polvilho seco dura até 1 ano</td></tr>
              </tbody>
            </table>""",
            "dicas": """
            <ul>
              <li>Não confunda aluvião (rio) com filão (rocha).</li>
              <li>Bandeiras = São Paulo; açúcar no início = São Vicente.</li>
              <li>Quilombo é resistência, não engenho.</li>
              <li>Na pergunta sobre os Suiá, lembre: seca = ralar e secar; cestos = homens.</li>
              <li>Conservar alimento = fazê-lo durar mais tempo sem estragar.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "No reino do Congo, os comerciantes usavam como moeda conchas chamadas:",
                ["Nzimbu", "Bateia", "Filão", "Beiju"],
                0,
                "Nzimbu eram conchas usadas nas trocas do reino do Congo.",
                "Resposta correta: nzimbu.",
            ),
            _mc(
                "Njinga a Mbande ficou conhecida por ser:",
                [
                    "Uma bandeirante paulista",
                    "Uma rainha do Ndongo que resistiu aos portugueses",
                    "Uma navegadora portuguesa",
                    "Uma tropeira de Minas Gerais",
                ],
                1,
                "Njinga liderou o Ndongo e resistiu à ocupação portuguesa.",
                "Resposta correta: uma rainha do Ndongo que resistiu aos portugueses.",
            ),
            _mc(
                "Historiadores chamam de diáspora africana:",
                [
                    "Uma festa tradicional do Congo",
                    "Um tipo de engenho de açúcar",
                    "A dispersão forçada de africanos para outros continentes",
                    "Uma moeda usada no Brasil colonial",
                ],
                2,
                "Diáspora = espalhamento forçado de povos africanos pelo tráfico.",
                "Resposta correta: a dispersão forçada de africanos para outros continentes.",
            ),
            _mc(
                "Os quilombos eram:",
                [
                    "Engenhos de açúcar no litoral",
                    "Fortes portugueses na África",
                    "Vilas criadas por Portugal em Minas",
                    "Refúgios de pessoas que fugiam da escravização",
                ],
                3,
                "Quilombos foram espaços de resistência e liberdade.",
                "Resposta correta: refúgios de pessoas que fugiam da escravização.",
            ),
            _mc(
                "Em 1532, Martim Afonso de Sousa fundou, no litoral paulista, a vila de:",
                ["São Vicente", "Ouro Preto", "Recife", "Belém"],
                0,
                "São Vicente foi uma das primeiras vilas e teve um dos primeiros engenhos.",
                "Resposta correta: São Vicente.",
            ),
            _mc(
                "De onde partiam as bandeiras rumo ao sertão no século XVII?",
                ["Salvador", "São Paulo de Piratininga", "Recife", "Belém"],
                1,
                "A vila paulista no planalto era o ponto de partida das bandeiras.",
                "Resposta correta: São Paulo de Piratininga.",
            ),
            _mc(
                "O ouro que fica preso em um veio dentro da rocha é chamado de:",
                ["Aluvião", "Nzimbu", "Filão", "Bateia"],
                2,
                "Filão = veio na rocha; aluvião = partículas na areia dos rios.",
                "Resposta correta: filão.",
            ),
            _mc(
                "Os tropeiros eram importantes para a região das minas porque:",
                [
                    "Governavam as vilas mineradoras",
                    "Fundaram São Vicente",
                    "Comandavam navios negreiros",
                    "Levavam alimentos e mercadorias em mulas até as minas",
                ],
                3,
                "Mineradores não tinham tempo de plantar; tropeiros traziam comida de outras regiões.",
                "Resposta correta: levavam alimentos e mercadorias em mulas até as minas.",
            ),
            _mc(
                "Por que as mulheres Suiá ralam a mandioca na época da seca?",
                [
                    "Para o polvilho secar bem ao sol e poder ser guardado",
                    "Porque a mandioca só nasce na seca",
                    "Para vender aos tropeiros",
                    "Porque na seca os homens não trabalham",
                ],
                0,
                "Sem chuva, o polvilho seca ao sol e pode ser armazenado por muito tempo.",
                "Resposta correta: para o polvilho secar bem ao sol e poder ser guardado.",
            ),
            _mc(
                "No povo Suiá, quem faz os cestos usados para guardar o polvilho?",
                ["As mulheres", "As crianças", "Os homens", "Os visitantes"],
                2,
                "O texto informa que os homens fazem os cestos; as mulheres ralam a mandioca.",
                "Resposta correta: os homens.",
            ),
            _sa(
                "Explique uma técnica que o povo Suiá desenvolveu para conservar alimentos.",
                ["polvilho", "secar", "seca", "cesto", "guardar", "um ano"],
                "Os Suiá secam o polvilho na época da seca e o guardam em cestos, fazendo-o durar até um ano.",
                "Resposta esperada: secar o polvilho da mandioca ao sol na época da seca e guardá-lo em cestos — assim ele dura até um ano.",
            ),
        ],
    }


def _subject_geografia() -> dict:
    return {
        "title": "Geografia",
        "icon": "GE",
        "sections": {
            "percurso": f"""
            <p>Conteúdo dos <strong>Módulos 10, 11 e 12</strong>: linhas imaginárias, zonas térmicas, climas do Brasil,
            paisagens urbanas e rurais, consumo responsável e leitura da conta de luz.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Linhas imaginárias</h3>
            <ul>
              <li><span class="hl">Equador</span> — paralelo 0°; divide o planeta em hemisférios <strong>Norte e Sul</strong>. No Brasil, passa por <strong>Macapá</strong> (AP).</li>
              <li><span class="hl">Meridiano de Greenwich</span> — meridiano 0°; divide <strong>Leste (Oriental) e Oeste (Ocidental)</strong>.</li>
              <li><span class="hl">Trópicos</span> — Câncer (Norte) e Capricórnio (Sul); o de Capricórnio corta MS, SP e PR.</li>
            </ul>

            <h3>2. Zonas térmicas</h3>
            <p>Perto do Equador os raios do Sol chegam mais <strong>perpendiculares</strong> e esquentam mais.
            A maior parte do Brasil fica na <strong>zona intertropical</strong> (quente). SC e RS ficam na zona temperada Sul, com inverno mais frio.</p>

            <h3>3. Climas do Brasil</h3>
            <ul>
              <li><strong>Equatorial</strong> — quente e úmido o ano todo (Norte).</li>
              <li><strong>Tropical semiárido</strong> — pouca chuva, secas longas (interior do Nordeste).</li>
              <li><strong>Subtropical</strong> — quatro estações, inverno frio (Sul).</li>
            </ul>

            <h3>4. Zona rural e zona urbana</h3>
            <p>O município tem <strong>campo</strong> (zona rural) e <strong>cidade</strong> (zona urbana).</p>
            <ul>
              <li><span class="hl">Rural</span> — agricultura, pecuária e extrativismo = <strong>setor primário</strong> (matérias-primas e alimentos).</li>
              <li><span class="hl">Indústria</span> — transforma matérias-primas = <strong>setor secundário</strong>.</li>
              <li><span class="hl">Urbana</span> — comércio, serviços e indústria.</li>
            </ul>
            <p>Campo e cidade são <strong>interdependentes</strong>: o campo fornece alimentos; a cidade fornece máquinas, remédios, vacinas e celulares.</p>

            <h3>5. Consumo responsável e conta de luz</h3>
            <p>Consumir com responsabilidade é <strong>evitar desperdício</strong> de água, energia e produtos.</p>
            <ul>
              <li>A energia elétrica é medida em <span class="hl">quilowatt-hora (kWh)</span>.</li>
              <li><strong>Consumo do mês = leitura atual − leitura anterior</strong> do medidor.</li>
              <li>A conta traz dados do cliente, dados de medição, vencimento e histórico de consumo (gráfico de barras).</li>
            </ul>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Apagar luzes ao sair, tomar banhos rápidos e reaproveitar brinquedos e roupas são atitudes de consumo responsável.
            </div>""",
            "resumo": """
            <h3>Linhas imaginárias</h3>
            <table>
              <thead><tr><th>Linha</th><th>Divide</th></tr></thead>
              <tbody>
                <tr><td>Equador (0°)</td><td>Norte · Sul</td></tr>
                <tr><td>Greenwich (0°)</td><td>Leste (Oriental) · Oeste (Ocidental)</td></tr>
                <tr><td>Trópico de Capricórnio</td><td>Zona intertropical · temperada Sul</td></tr>
              </tbody>
            </table>

            <h3>Climas</h3>
            <table>
              <thead><tr><th>Clima</th><th>Marca</th></tr></thead>
              <tbody>
                <tr><td>Equatorial</td><td>Quente e úmido o ano todo</td></tr>
                <tr><td>Tropical semiárido</td><td>Pouca chuva — seca</td></tr>
                <tr><td>Subtropical</td><td>Inverno frio — Sul</td></tr>
              </tbody>
            </table>

            <h3>Campo e cidade</h3>
            <table>
              <thead><tr><th>Zona</th><th>Atividades</th><th>Setor</th></tr></thead>
              <tbody>
                <tr><td>Rural</td><td>Agricultura · pecuária · extrativismo</td><td>Primário</td></tr>
                <tr><td>Urbana</td><td>Indústria</td><td>Secundário</td></tr>
                <tr><td>Urbana</td><td>Comércio · serviços</td><td>Terciário</td></tr>
              </tbody>
            </table>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Conta de luz: consumo = leitura atual − leitura anterior (em kWh).
            </div>""",
            "dicas": """
            <ul>
              <li>Equador = Norte/Sul; Greenwich = Leste/Oeste. Não troque!</li>
              <li>Macapá é a capital cortada pela linha do Equador.</li>
              <li>Na conta de luz, faça a subtração das leituras com calma.</li>
              <li>Setor primário = produz no campo; secundário = transforma na indústria.</li>
              <li>Consumo responsável = economizar e evitar desperdício, não «nunca comprar».</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "A linha do Equador divide o planeta em hemisférios:",
                ["Leste e Oeste", "Norte e Sul", "Rural e urbano", "Oriental e Polar"],
                1,
                "O Equador (paralelo 0°) separa o hemisfério Norte do hemisfério Sul.",
                "Resposta correta: Norte e Sul.",
            ),
            _mc(
                "O meridiano de Greenwich (0°) divide a Terra em hemisférios:",
                ["Oriental (Leste) e Ocidental (Oeste)", "Norte e Sul", "Polar e temperado", "Campo e cidade"],
                0,
                "Greenwich separa Leste e Oeste.",
                "Resposta correta: Oriental (Leste) e Ocidental (Oeste).",
            ),
            _mc(
                "A maior parte do território brasileiro está em qual zona térmica?",
                ["Polar", "Temperada Norte", "Intertropical", "Temperada Sul"],
                2,
                "Quase todo o Brasil fica entre os trópicos — zona intertropical, mais quente.",
                "Resposta correta: intertropical.",
            ),
            _mc(
                "O clima tropical semiárido, do interior do Nordeste, tem como característica:",
                ["Neve frequente no inverno", "Pouca chuva e secas longas", "Chuva forte o ano todo", "Quatro estações bem definidas"],
                1,
                "Semiárido = pouca chuva; a vegetação típica é a Caatinga.",
                "Resposta correta: pouca chuva e secas longas.",
            ),
            _mc(
                "Quais atividades econômicas predominam na zona rural?",
                [
                    "Comércio e bancos",
                    "Indústria de automóveis",
                    "Shoppings e escritórios",
                    "Agricultura, pecuária e extrativismo",
                ],
                3,
                "O campo produz alimentos e matérias-primas — setor primário.",
                "Resposta correta: agricultura, pecuária e extrativismo.",
            ),
            _mc(
                "A indústria, que transforma matérias-primas em produtos, faz parte do setor:",
                ["Primário", "Secundário", "Rural", "Polar"],
                1,
                "Setor secundário = indústria; primário = campo; terciário = comércio e serviços.",
                "Resposta correta: secundário.",
            ),
            _mc(
                "Campo e cidade são interdependentes. Um exemplo do que a cidade fornece ao campo é:",
                ["Leite e feijão", "Trigo e arroz", "Máquinas, vacinas e celulares", "Frutas colhidas no pé"],
                2,
                "O campo fornece alimentos; a cidade fornece produtos industriais e serviços.",
                "Resposta correta: máquinas, vacinas e celulares.",
            ),
            _mc(
                "Na conta de luz de uma casa, a leitura anterior do medidor foi 3.740 kWh e a leitura atual foi 3.900 kWh. "
                "Qual foi o consumo do mês?",
                ["160 kWh", "7.640 kWh", "260 kWh", "140 kWh"],
                0,
                "Consumo = leitura atual − leitura anterior = 3.900 − 3.740 = 160 kWh.",
                "Resposta correta: 160 kWh.",
            ),
            _mc(
                "Qual atitude é um exemplo de consumo responsável de energia elétrica?",
                [
                    "Deixar a TV ligada sem ninguém assistindo",
                    "Abrir a geladeira muitas vezes sem necessidade",
                    "Apagar as luzes ao sair de um cômodo",
                    "Tomar banhos bem demorados",
                ],
                2,
                "Apagar luzes evita desperdício e diminui a conta.",
                "Resposta correta: apagar as luzes ao sair de um cômodo.",
            ),
            _mc(
                "Na conta de luz, a sigla kWh é a abreviatura de:",
                ["Quilograma por hora", "Quilômetro por hora", "Quilowatt por mês", "Quilowatt-hora"],
                3,
                "A unidade de consumo de energia elétrica é o quilowatt-hora (kWh).",
                "Resposta correta: quilowatt-hora.",
            ),
            _sa(
                "Cite uma medida para economizar energia elétrica e uma para economizar água em casa.",
                ["apagar", "luz", "desligar", "banho", "torneira", "fechar"],
                "Exemplos: apagar luzes e desligar aparelhos; tomar banho rápido e fechar a torneira ao escovar os dentes.",
                "Resposta esperada: energia — apagar a luz ao sair do cômodo; água — fechar a torneira ao escovar os dentes ou tomar banho rápido.",
            ),
        ],
    }


def _subject_ciencias() -> dict:
    return {
        "title": "Ciências",
        "icon": "CI",
        "sections": {
            "percurso": f"""
            <p>Conteúdo dos <strong>Módulos 10 a 14</strong>: microrganismos, higiene, leveduras e fermentação,
            antibióticos e vacinas, misturas homogêneas e heterogêneas e soluções.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Microrganismos</h3>
            <p>São seres vivos tão pequenos que só vemos com <strong>microscópio</strong>: bactérias, fungos e vírus.</p>
            <ul>
              <li>Alguns causam doenças (<span class="hl">patogênicos</span>): mofo no pão, cárie, gripe.</li>
              <li>Outros são úteis: <strong>lactobacilos</strong> ajudam na digestão; fungos e bactérias decompõem restos na compostagem.</li>
            </ul>
            <p>No laboratório, cultivam-se microrganismos na <strong>placa de Petri</strong> com <strong>meio de cultura</strong> (nutrientes).
            Lavar as mãos com água e sabão por 20 segundos reduz muito os microrganismos.</p>

            <h3>2. Leveduras e fermentação</h3>
            <p>O <span class="hl">fermento biológico</span> tem leveduras — fungos microscópicos. Elas se alimentam do açúcar
            e liberam <strong>gás carbônico</strong>, que forma bolhas e faz a massa do pão crescer (os «furinhos»).
            Leveduras também fermentam a cana-de-açúcar para produzir <strong>etanol</strong> (álcool combustível).</p>

            <h3>3. Antibióticos e vacinas</h3>
            <ul>
              <li><span class="hl">Antibiótico</span> — trata infecções causadas por <strong>bactérias</strong>. Não funciona contra vírus (como o da gripe). Só com receita médica.</li>
              <li><span class="hl">Vacina</span> — <strong>previne</strong> doenças: prepara as defesas do corpo antes do contato com o microrganismo.</li>
            </ul>
            <p>A penicilina foi descoberta por Alexander Fleming a partir de um fungo.</p>

            <h3>4. Misturas</h3>
            <p>Quando juntamos dois ou mais componentes, formamos uma <strong>mistura</strong>.</p>
            <ul>
              <li><span class="hl">Homogênea</span> — aspecto uniforme, não dá para ver os componentes: água com açúcar, café, chá, ar.</li>
              <li><span class="hl">Heterogênea</span> — dá para ver os componentes separados: água e óleo, água e areia, rochas (minerais diferentes).</li>
            </ul>

            <h3>5. Soluções</h3>
            <p>Solução é uma mistura homogênea. O que <strong>dissolve</strong> é o <span class="hl">solvente</span>;
            o que <strong>é dissolvido</strong> é o <span class="hl">soluto</span>. Na água com corante, a água é o solvente e o corante é o soluto.
            A água é chamada de <strong>solvente universal</strong> porque dissolve muitas substâncias.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Areia e óleo <strong>não se dissolvem</strong> na água — por isso formam misturas heterogêneas, não soluções.
            </div>""",
            "resumo": """
            <h3>Microrganismos</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Exemplo ruim</th><th>Exemplo útil</th></tr></thead>
              <tbody>
                <tr><td>Bactéria</td><td>Cárie</td><td>Lactobacilos (digestão)</td></tr>
                <tr><td>Fungo</td><td>Mofo no pão</td><td>Levedura (pão, etanol) · penicilina</td></tr>
                <tr><td>Vírus</td><td>Gripe, resfriado</td><td>—</td></tr>
              </tbody>
            </table>

            <h3>Vacina × antibiótico</h3>
            <table>
              <thead><tr><th></th><th>Vacina</th><th>Antibiótico</th></tr></thead>
              <tbody>
                <tr><td>Para quê</td><td>Prevenir</td><td>Tratar infecção</td></tr>
                <tr><td>Contra</td><td>Vírus e bactérias</td><td>Só bactérias</td></tr>
              </tbody>
            </table>

            <h3>Misturas</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Aspecto</th><th>Exemplos</th></tr></thead>
              <tbody>
                <tr><td>Homogênea (solução)</td><td>Uniforme</td><td>Água com açúcar · café · ar</td></tr>
                <tr><td>Heterogênea</td><td>Partes visíveis</td><td>Água e óleo · água e areia · rocha</td></tr>
              </tbody>
            </table>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Soluto = é dissolvido (açúcar). Solvente = dissolve (água).
            </div>""",
            "dicas": """
            <ul>
              <li>Gripe é vírus → antibiótico não resolve.</li>
              <li>Vacina previne; antibiótico trata.</li>
              <li>Furinhos no pão = gás carbônico das leveduras.</li>
              <li>Se dá para ver as partes separadas, a mistura é heterogênea.</li>
              <li>Na solução, o solvente geralmente está em maior quantidade (muitas vezes, a água).</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Microrganismos são:",
                [
                    "Todos prejudiciais à saúde",
                    "Seres vivos tão pequenos que só vemos com microscópio",
                    "Pedrinhas minúsculas sem vida",
                    "Animais que vivem só no mar",
                ],
                1,
                "Bactérias, fungos e vírus são microscópicos; muitos são úteis.",
                "Resposta correta: seres vivos tão pequenos que só vemos com microscópio.",
            ),
            _mc(
                "Os lactobacilos que vivem no nosso intestino:",
                ["Ajudam na digestão", "Causam cárie", "Provocam gripe", "Estragam o pão"],
                0,
                "Lactobacilos são exemplos de microrganismos benéficos.",
                "Resposta correta: ajudam na digestão.",
            ),
            _mc(
                "No laboratório, o meio de cultura colocado na placa de Petri serve para:",
                [
                    "Matar todas as bactérias",
                    "Medir a temperatura da sala",
                    "Oferecer nutrientes para os microrganismos crescerem",
                    "Guardar vacinas",
                ],
                2,
                "O meio de cultura tem nutrientes que favorecem a multiplicação de fungos e bactérias.",
                "Resposta correta: oferecer nutrientes para os microrganismos crescerem.",
            ),
            _mc(
                "Qual destas misturas é heterogênea?",
                ["Água com açúcar dissolvido", "Café coado", "Chá de camomila", "Água e óleo"],
                3,
                "O óleo não se dissolve e fica separado da água — dá para ver os componentes.",
                "Resposta correta: água e óleo.",
            ),
            _mc(
                "Um corante foi colocado na água e se dissolveu totalmente, formando uma solução. Nessa solução, o solvente é:",
                ["O corante", "A água", "O copo", "A colher"],
                1,
                "Solvente é o que dissolve (água); soluto é o que é dissolvido (corante).",
                "Resposta correta: a água.",
            ),
            _mc(
                "Misturando areia e água, depois de alguns segundos a areia vai para o fundo. Essa mistura é:",
                [
                    "Uma solução, porque a areia se dissolveu",
                    "Heterogênea, porque a areia não se dissolve na água",
                    "Homogênea, porque tem aspecto uniforme",
                    "Uma substância pura",
                ],
                1,
                "A areia não se dissolve e fica visível no fundo — mistura heterogênea.",
                "Resposta correta: heterogênea, porque a areia não se dissolve na água.",
            ),
            _mc(
                "O ar que respiramos, formado por gás nitrogênio, gás oxigênio, gás carbônico e vapor de água, é:",
                [
                    "Uma mistura de gases",
                    "Uma única substância",
                    "Uma mistura de óleo e água",
                    "Apenas gás oxigênio",
                ],
                0,
                "O ar é uma mistura gasosa: os gases se misturam totalmente.",
                "Resposta correta: uma mistura de gases.",
            ),
            _mc(
                "Os furinhos dentro de uma fatia de pão feito com fermento biológico aparecem porque:",
                [
                    "A farinha tem buracos naturais",
                    "O sal derrete no forno",
                    "As leveduras liberam gás carbônico na fermentação",
                    "O óleo evapora da massa",
                ],
                2,
                "Leveduras consomem açúcar e liberam gás carbônico, que forma bolhas na massa.",
                "Resposta correta: as leveduras liberam gás carbônico na fermentação.",
            ),
            _mc(
                "No Brasil, o etanol (álcool combustível) é produzido principalmente pela fermentação da:",
                ["Cana-de-açúcar", "Areia", "Água mineral", "Mandioca seca"],
                0,
                "Leveduras fermentam o caldo da cana e produzem etanol nas usinas.",
                "Resposta correta: cana-de-açúcar.",
            ),
            _mc(
                "Por que o antibiótico não cura a gripe?",
                [
                    "Porque a gripe é causada por bactérias resistentes",
                    "Porque o antibiótico só funciona em crianças",
                    "Porque a gripe não é uma doença",
                    "Porque a gripe é causada por vírus, e o antibiótico age contra bactérias",
                ],
                3,
                "Antibióticos combatem bactérias; vírus não são afetados por eles.",
                "Resposta correta: porque a gripe é causada por vírus, e o antibiótico age contra bactérias.",
            ),
            _sa(
                "Explique a diferença entre vacina e antibiótico.",
                ["prevenir", "previne", "tratar", "trata", "bactéria", "defesa"],
                "Vacina prepara as defesas do corpo antes da doença; antibiótico trata infecções por bactérias.",
                "Resposta esperada: a vacina previne doenças, preparando as defesas do corpo; o antibiótico trata infecções já causadas por bactérias.",
            ),
        ],
    }


def _subject_matematica() -> dict:
    return {
        "title": "Matemática",
        "icon": "MA",
        "sections": {
            "percurso": f"""
            <p>Conteúdo do 3º trimestre: <strong>números decimais</strong> (décimos e centésimos), comparação e ordenação,
            reta numérica, <strong>sistema monetário</strong> e <strong>medidas de massa</strong> (mg, g, kg, t).</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Números decimais</h3>
            <p>Aparecem na balança (66,6 kg), no termômetro (36,3 °C) e nos preços (R$ 4,50).</p>
            <ul>
              <li><span class="hl">Décimo</span> — a unidade dividida em 10 partes: 1 ÷ 10 = 0,1. <strong>10 décimos = 1 inteiro.</strong></li>
              <li><span class="hl">Centésimo</span> — a unidade dividida em 100 partes: 1 ÷ 100 = 0,01.</li>
              <li>Metade de 1 inteiro = 0,5.</li>
            </ul>

            <h3>2. Comparar e ordenar</h3>
            <p>Compare primeiro a <strong>parte inteira</strong>; se for igual, compare os décimos, depois os centésimos.</p>
            <ul>
              <li>3,5 &gt; 3,05 (5 décimos é mais que 0 décimo).</li>
              <li>2,7 e 2,70 são o <strong>mesmo número</strong>.</li>
            </ul>

            <h3>3. Reta numérica</h3>
            <p>De 0 a 1 dividido em 10 partes iguais, cada tracinho vale <strong>0,1</strong>: 0 · 0,1 · 0,2 · … · 0,9 · 1.</p>

            <h3>4. Sistema monetário</h3>
            <p>R$ 42,75 lê-se «quarenta e dois reais e setenta e cinco centavos». <strong>100 centavos = R$ 1,00.</strong></p>
            <p><span class="hl">Troco</span> = valor pago − preço. Alinhe as vírgulas antes de somar ou subtrair.</p>

            <h3>5. Medidas de massa</h3>
            <p>Usamos a <strong>balança</strong> para medir massa. Unidades:</p>
            <ul>
              <li><strong>1 t = 1.000 kg</strong> (tonelada — caminhões)</li>
              <li><strong>1 kg = 1.000 g</strong> (quilograma — pessoas, farinha)</li>
              <li><strong>1 g = 1.000 mg</strong> (miligrama — remédios, vitaminas)</li>
            </ul>
            <p>No rótulo: <strong>peso bruto</strong> = produto + embalagem; <strong>peso líquido</strong> = só o produto.
            A antiga <strong>arroba</strong> vale cerca de 15 kg.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Para passar de kg para g, multiplique por 1.000. Para passar de g para kg, divida por 1.000 (500 g = 0,5 kg).
            </div>""",
            "resumo": """
            <h3>Decimais</h3>
            <table>
              <thead><tr><th>Nome</th><th>Fração da unidade</th><th>Escrita</th></tr></thead>
              <tbody>
                <tr><td>Décimo</td><td>1 de 10 partes</td><td>0,1</td></tr>
                <tr><td>Centésimo</td><td>1 de 100 partes</td><td>0,01</td></tr>
                <tr><td>Metade</td><td>5 de 10 partes</td><td>0,5</td></tr>
              </tbody>
            </table>

            <h3>Dinheiro</h3>
            <table>
              <thead><tr><th>Escrita</th><th>Leitura</th></tr></thead>
              <tbody>
                <tr><td>R$ 0,50</td><td>cinquenta centavos</td></tr>
                <tr><td>R$ 3,75</td><td>três reais e setenta e cinco centavos</td></tr>
                <tr><td>R$ 1,00</td><td>um real = 100 centavos</td></tr>
              </tbody>
            </table>

            <h3>Massa</h3>
            <table>
              <thead><tr><th>Relação</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>1 t = 1.000 kg</td><td>16 t = 16.000 kg</td></tr>
                <tr><td>1 kg = 1.000 g</td><td>2,5 kg = 2.500 g</td></tr>
                <tr><td>1 g = 1.000 mg</td><td>2.500 mg = 2,5 g</td></tr>
              </tbody>
            </table>""",
            "dicas": """
            <ul>
              <li>Mais algarismos depois da vírgula não quer dizer número maior: 3,05 &lt; 3,5.</li>
              <li>Na reta de 0 a 1 com 10 partes, conte os tracinhos: cada um vale 0,1.</li>
              <li>Em troco, monte a conta com vírgula embaixo de vírgula.</li>
              <li>Peso líquido = peso bruto − embalagem.</li>
              <li>Antes de comparar massas, deixe todas na mesma unidade.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Quantos décimos formam uma unidade inteira?",
                ["2", "5", "10", "100"],
                2,
                "0,1 dez vezes = 1. Dez décimos formam um inteiro.",
                "Resposta correta: 10.",
            ),
            _mc(
                "Qual comparação está correta?",
                ["3,05 > 3,5", "3,5 > 3,05", "3,5 = 3,05", "3,05 = 3,50"],
                1,
                "Mesma parte inteira (3); nos décimos, 5 > 0. Então 3,5 > 3,05.",
                "Resposta correta: 3,5 > 3,05.",
            ),
            _mc(
                "Qual opção mostra os números 2,7 · 2,07 · 2,5 em ordem crescente (do menor para o maior)?",
                ["2,7 · 2,5 · 2,07", "2,5 · 2,07 · 2,7", "2,07 · 2,5 · 2,7", "2,07 · 2,7 · 2,5"],
                2,
                "Décimos: 2,07 tem 0, 2,5 tem 5, 2,7 tem 7 → 2,07 < 2,5 < 2,7.",
                "Resposta correta: 2,07 · 2,5 · 2,7.",
            ),
            _mc(
                "Uma reta numérica vai de 0 a 1 e está dividida em 10 partes iguais. Que número fica no 4º tracinho depois do 0?",
                ["0,4", "4", "0,04", "40"],
                0,
                "Cada parte vale 0,1; quatro partes = 0,4.",
                "Resposta correta: 0,4.",
            ),
            _mc(
                "Como se lê o valor R$ 42,75?",
                [
                    "Quatrocentos e vinte e sete reais e cinco centavos",
                    "Quarenta e dois reais e sete centavos",
                    "Quatro reais e duzentos e setenta e cinco centavos",
                    "Quarenta e dois reais e setenta e cinco centavos",
                ],
                3,
                "Antes da vírgula, reais (42); depois da vírgula, centavos (75).",
                "Resposta correta: quarenta e dois reais e setenta e cinco centavos.",
            ),
            _mc(
                "Benjamin comprou um livro de R$ 13,40 e pagou com uma nota de R$ 20,00. Quanto recebeu de troco?",
                ["R$ 7,60", "R$ 6,60", "R$ 6,40", "R$ 33,40"],
                1,
                "20,00 − 13,40 = 6,60.",
                "Resposta correta: R$ 6,60.",
            ),
            _mc(
                "Um saco de farinha tem 2,5 kg. Quantos gramas são?",
                ["250 g", "25 g", "2.500 g", "25.000 g"],
                2,
                "1 kg = 1.000 g → 2,5 × 1.000 = 2.500 g.",
                "Resposta correta: 2.500 g.",
            ),
            _mc(
                "No rótulo de um produto: peso bruto (produto + embalagem) = 0,160 kg; peso da embalagem = 0,005 kg. "
                "Qual é o peso líquido, em gramas?",
                ["165 g", "160 g", "150 g", "155 g"],
                3,
                "0,160 kg = 160 g; 0,005 kg = 5 g. Líquido = 160 − 5 = 155 g.",
                "Resposta correta: 155 g.",
            ),
            _mc(
                "Uma águia tem massa de 5.500 g e consegue levantar uma presa de até 4 vezes a sua massa. "
                "Qual é a massa máxima dessa presa, em quilogramas?",
                ["22 kg", "9,5 kg", "2,2 kg", "220 kg"],
                0,
                "5.500 × 4 = 22.000 g; 22.000 ÷ 1.000 = 22 kg.",
                "Resposta correta: 22 kg.",
            ),
            _mc(
                "Um caminhão tem massa de 16 toneladas. Quanto é isso em quilogramas?",
                ["1.600 kg", "160 kg", "16.000 kg", "160.000 kg"],
                2,
                "1 t = 1.000 kg → 16 × 1.000 = 16.000 kg.",
                "Resposta correta: 16.000 kg.",
            ),
            _sa(
                "Escreva 500 g em quilogramas.",
                ["0,5", "0,500", "meio"],
                "500 ÷ 1.000 = 0,5 kg — meio quilo.",
                "Resposta esperada: 0,5 kg (meio quilograma).",
            ),
            _sa(
                "Uma arroba equivale a aproximadamente 15 kg. Quantos quilogramas são, aproximadamente, 3 arrobas?",
                ["45"],
                "3 × 15 = 45 kg.",
                "Resposta esperada: aproximadamente 45 kg.",
            ),
        ],
    }


def build_simulado() -> dict:
    return {
        "title": "Simulado da PI",
        "icon": "★",
        "intro": """Um teste com <strong>20 questões</strong> (4 por disciplina), todas de múltipla escolha,
              ligadas ao texto abaixo sobre a «Feira de Ciências da Escola Verde» e ao conteúdo das abas.""",
        "textTitle": "Texto-base — Feira de Ciências da Escola Verde",
        "text": """
            <p>Na <strong>Feira de Ciências da Escola Verde</strong>, a turma do 4º ano montou estandes sobre a horta da escola.
            No palco, um grupo encenou um trecho de <strong>«Viravez, o cortês»</strong>: Viravez soltou o Saci e ganhou muita comida,
            mas disse à esposa Inácia, que estava <em>descrente</em>, que era «herança do tio Hipólito». Um painel lembrava que
            <strong>Tarsila do Amaral</strong> pintou o Abaporu em 1928: «Ela usou as cores caipiras de que gostava desde a infância».
            Outro cartaz recontava a lenda <strong>«A origem da lavoura»</strong>, em que uma moça desce do céu com a chuva e ensina a plantar.</p>

            <p>No estande de Ciências, a turma fez pão caseiro seguindo um <strong>cartaz instrucional</strong>:
            «Materiais: 1 kg de farinha, fermento biológico, água, açúcar e sal. Passos: 1) misture; 2) sove; 3) deixe descansar
            1 hora; 4) asse.» O fermento biológico tem <strong>leveduras</strong>, fungos microscópicos que liberam gás carbônico e
            fazem a massa crescer. Na mesa das misturas havia um copo de <strong>água com açúcar</strong> dissolvido e outro de
            <strong>água com óleo</strong>, com o óleo boiando por cima. Um cartaz de saúde dizia: «Vacinas preparam as defesas do corpo
            antes da doença; antibióticos tratam infecções causadas por bactérias.»</p>

            <p>Em História, a turma apresentou o <strong>polvilho do povo Suiá</strong>, do Xingu: na época da seca, as
            <strong>mulheres</strong> ralam a mandioca para o polvilho secar ao sol, e os <strong>homens</strong> fazem cestos para
            guardá-lo; assim, o polvilho dura até um ano. Uma linha do tempo mostrava <strong>1532</strong>, quando Martim Afonso de Sousa
            fundou São Vicente e logo surgiram engenhos de açúcar, e o ouro de <strong>aluvião</strong>, encontrado em partículas na areia
            dos rios de Minas Gerais. No <strong>mapa do Brasil</strong>, a linha do Equador passava por <strong>Macapá</strong>, e uma
            legenda explicava que a mandioca vem da <strong>zona rural</strong>, onde há agricultura, pecuária e extrativismo
            (setor primário).</p>

            <p>Na barraca de Matemática, o pão custava <strong>R$ 3,50</strong> e o suco, <strong>R$ 2,75</strong>; cada pacote de
            polvilho tinha <strong>500 g</strong>. A turma também mediu três mudas da horta: 0,8 m, 0,45 m e 0,6 m. Por fim, conferiu a
            <strong>conta de luz</strong> da escola: leitura anterior de 2.340 kWh e leitura atual de 2.520 kWh. O consumo do mês é a
            diferença entre as duas leituras, medido em quilowatt-hora (kWh).</p>""",
        "questions": [
            {
                "discipline": "Língua Portuguesa",
                "question": "Por que Viravez diz a Inácia que a comida é «herança do tio Hipólito»?",
                "options": [
                    "Para esconder que a comida veio do Saci",
                    "Porque o tio realmente deixou a comida",
                    "Para vender a comida na feira",
                    "Porque Inácia pediu uma herança",
                ],
                "correctAnswer": 0,
                "explanation": "Viravez ganhou a comida do Saci e precisa guardar segredo — por isso inventa a herança.",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "No painel, «Ela usou as cores caipiras de que gostava desde a infância». O pronome «Ela» se refere a:",
                "options": ["Inácia", "Tarsila do Amaral", "A moça da lenda", "A turma do 4º ano"],
                "correctAnswer": 1,
                "explanation": "A frase anterior fala de Tarsila do Amaral; o pronome pessoal «Ela» retoma esse nome.",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "O que mostra que o cartaz do pão é um texto instrucional?",
                "options": [
                    "Tem rimas no final de cada linha",
                    "Tem diálogos com travessão",
                    "Apresenta materiais e passos numerados em ordem",
                    "Dá a opinião do autor sobre o pão",
                ],
                "correctAnswer": 2,
                "explanation": "Texto instrucional ensina a fazer algo: lista materiais e passos em sequência.",
            },
            {
                "discipline": "Língua Portuguesa",
                "question": "A lenda «A origem da lavoura», recontada no cartaz, é um texto que:",
                "options": [
                    "Conta só fatos reais, com datas exatas",
                    "É uma notícia de jornal",
                    "Não tem personagens",
                    "Mistura fantasia e realidade para explicar algo da natureza",
                ],
                "correctAnswer": 3,
                "explanation": "A moça vinda do céu é fantasia; a chuva ajudar a lavoura é real — marca das lendas.",
            },
            {
                "discipline": "História",
                "question": "Segundo o texto, no povo Suiá quem rala a mandioca para fazer o polvilho?",
                "options": ["Os homens", "As crianças", "As mulheres", "Os tropeiros"],
                "correctAnswer": 2,
                "explanation": "O texto diz que as mulheres ralam a mandioca na época da seca.",
            },
            {
                "discipline": "História",
                "question": "Guardado nos cestos feitos pelos homens, o polvilho Suiá dura até:",
                "options": ["Uma semana", "Um ano", "Um mês", "Dez anos"],
                "correctAnswer": 1,
                "explanation": "O texto informa que o polvilho seco dura até um ano.",
            },
            {
                "discipline": "História",
                "question": "De acordo com a linha do tempo, em 1532 Martim Afonso de Sousa fundou:",
                "options": ["Ouro Preto", "Salvador", "Mariana", "São Vicente"],
                "correctAnswer": 3,
                "explanation": "1532 = fundação de São Vicente, seguida pelos primeiros engenhos de açúcar.",
            },
            {
                "discipline": "História",
                "question": "O ouro de aluvião, citado na linha do tempo, é aquele encontrado:",
                "options": [
                    "Em partículas na areia dos rios",
                    "Em veios dentro das rochas",
                    "Nas plantações de cana",
                    "No fundo do mar",
                ],
                "correctAnswer": 0,
                "explanation": "O texto explica: aluvião = partículas de ouro na areia dos rios de Minas Gerais.",
            },
            {
                "discipline": "Geografia",
                "question": "Qual capital brasileira aparece no mapa da feira cortada pela linha do Equador?",
                "options": ["Belém", "Manaus", "Macapá", "Boa Vista"],
                "correctAnswer": 2,
                "explanation": "O texto cita que a linha do Equador passa por Macapá (AP).",
            },
            {
                "discipline": "Geografia",
                "question": "A produção de mandioca, segundo a legenda do mapa, pertence a qual zona e setor?",
                "options": [
                    "Zona rural — setor primário",
                    "Zona urbana — setor secundário",
                    "Zona urbana — comércio",
                    "Zona polar — indústria",
                ],
                "correctAnswer": 0,
                "explanation": "Agricultura é atividade da zona rural e faz parte do setor primário.",
            },
            {
                "discipline": "Geografia",
                "question": "Qual foi o consumo de energia elétrica da escola no mês?",
                "options": ["220 kWh", "180 kWh", "4.860 kWh", "18 kWh"],
                "correctAnswer": 1,
                "explanation": "Consumo = leitura atual − leitura anterior = 2.520 − 2.340 = 180 kWh.",
            },
            {
                "discipline": "Geografia",
                "question": "Qual atitude ajudaria a escola a diminuir a próxima conta de luz (consumo responsável)?",
                "options": [
                    "Deixar ventiladores ligados em salas vazias",
                    "Deixar computadores ligados a noite toda",
                    "Abrir a geladeira da cantina sem necessidade",
                    "Apagar as luzes ao sair das salas",
                ],
                "correctAnswer": 3,
                "explanation": "Apagar luzes evita desperdício de energia elétrica.",
            },
            {
                "discipline": "Ciências",
                "question": "Por que a massa do pão da feira cresceu?",
                "options": [
                    "As leveduras do fermento liberaram gás carbônico",
                    "O sal fez a massa inchar",
                    "A farinha absorveu ar sozinha",
                    "O óleo evaporou da massa",
                ],
                "correctAnswer": 0,
                "explanation": "O texto explica que as leveduras liberam gás carbônico e fazem a massa crescer.",
            },
            {
                "discipline": "Ciências",
                "question": "O copo de água com óleo, com o óleo boiando por cima, é um exemplo de:",
                "options": ["Mistura homogênea", "Solução", "Mistura heterogênea", "Substância pura"],
                "correctAnswer": 2,
                "explanation": "O óleo não se dissolve na água e as partes ficam visíveis — mistura heterogênea.",
            },
            {
                "discipline": "Ciências",
                "question": "No copo de água com açúcar dissolvido, o soluto é:",
                "options": ["A água", "O açúcar", "O copo", "O óleo"],
                "correctAnswer": 1,
                "explanation": "Soluto é o que se dissolve (açúcar); solvente é o que dissolve (água).",
            },
            {
                "discipline": "Ciências",
                "question": "Segundo o cartaz de saúde, as vacinas servem para:",
                "options": [
                    "Tratar infecções por bactérias já instaladas",
                    "Fazer a massa do pão crescer",
                    "Substituir a lavagem das mãos",
                    "Preparar as defesas do corpo antes da doença",
                ],
                "correctAnswer": 3,
                "explanation": "Vacinas previnem; tratar infecções por bactérias é papel dos antibióticos.",
            },
            {
                "discipline": "Matemática",
                "question": "A receita usa 1 kg de farinha. Quantos gramas são?",
                "options": ["10 g", "100 g", "1.000 g", "10.000 g"],
                "correctAnswer": 2,
                "explanation": "1 kg = 1.000 g.",
            },
            {
                "discipline": "Matemática",
                "question": "Um visitante comprou um pão e um suco e pagou com uma nota de R$ 10,00. Quanto recebeu de troco?",
                "options": ["R$ 3,75", "R$ 4,25", "R$ 6,25", "R$ 3,25"],
                "correctAnswer": 0,
                "explanation": "3,50 + 2,75 = 6,25; 10,00 − 6,25 = 3,75.",
            },
            {
                "discipline": "Matemática",
                "question": "Cada pacote de polvilho tem 500 g. Quanto é isso em quilogramas?",
                "options": ["5 kg", "0,5 kg", "50 kg", "0,05 kg"],
                "correctAnswer": 1,
                "explanation": "500 ÷ 1.000 = 0,5 kg (meio quilo).",
            },
            {
                "discipline": "Matemática",
                "question": "Qual opção mostra as alturas das mudas (0,8 m · 0,45 m · 0,6 m) em ordem crescente?",
                "options": [
                    "0,8 m · 0,6 m · 0,45 m",
                    "0,6 m · 0,45 m · 0,8 m",
                    "0,45 m · 0,8 m · 0,6 m",
                    "0,45 m · 0,6 m · 0,8 m",
                ],
                "correctAnswer": 3,
                "explanation": "Compare os décimos: 4 < 6 < 8 → 0,45 < 0,6 < 0,8.",
            },
        ],
    }
