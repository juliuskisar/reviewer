"""Conteúdo pedagógico da revisão PI — Pedro, 6º ano, 3º trimestre (Ciências + História)."""

from __future__ import annotations

REVIEW_ID = "pedro-pi-6ano-3tri"
STUDENT_NAME = "Pedro"
STUDENT_AGE = 12
GRADE = "6º ano"
PAGE_TITLE = f"Revisão Multidisciplinar — {STUDENT_NAME} ({GRADE}) · 3º trimestre"

PERCURSO_STEPS = """
            <ol>
              <li>Comece pelo <strong>Resumo</strong> para ver tabelas e ideias-chave.</li>
              <li>Depois leia a <strong>Conteúdo geral</strong> com calma.</li>
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
        "ciencias": _subject_ciencias(),
        "historia": _subject_historia(),
    }


def _subject_ciencias() -> dict:
    return {
        "title": "Ciências",
        "icon": "CI",
        "sections": {
            "percurso": f"""
            <p><strong>Módulo 25 — Óptica:</strong> fontes de luz, propagação, fenômenos ópticos.
            <strong>Módulo 26 — Lentes e visão:</strong> lentes convergentes e divergentes, foco,
            miopia e hipermetropia, astigmatismo.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Noções iniciais de óptica</h3>
            <p>Óptica estuda a <strong>luz</strong> — energia que permite ver o mundo. Analisamos
            emissão, <span class="hl">propagação</span> no meio (ar, água, vidro) e interação com espelhos,
            lentes, olho, câmeras.</p>
            <ul>
              <li><strong>Fontes primárias</strong> — emitem luz própria (Sol, vela acesa).</li>
              <li><strong>Fontes secundárias</strong> — refletem luz incidente (Lua, livro iluminado).</li>
              <li><strong>Pontuais</strong> — vistas como um ponto (estrela distante).</li>
              <li><strong>Extensas</strong> — tamanho apreciável (lâmpada fluorescente).</li>
            </ul>

            <h3>2. Fenômenos ópticos</h3>
            <ul>
              <li><strong>Reflexão difusa</strong> — superfície rugosa espalha a luz (folha verde vista como verde).</li>
              <li><strong>Absorção</strong> — corpo absorve algumas cores e reflete o pigmento.</li>
              <li><strong>Reflexão especular</strong> — superfície lisa forma imagem nítida (brilho na gota d'água).</li>
              <li><strong>Dispersão</strong> — luz branca separa-se em cores (arco-íris na asa do inseto).</li>
              <li><strong>Refração</strong> — luz muda de meio e pode desviar (gota funciona como lente).</li>
            </ul>

            <h3>3. Lentes esféricas</h3>
            <p><strong>Bordas finas</strong> → lente <span class="hl">convergente</span> — raios paralelos
            ao eixo principal encontram-se no <strong>foco real</strong>.</p>
            <p><strong>Bordas grossas</strong> → lente <span class="hl">divergente</span> — raios
            parecem «sair» de um <strong>foco virtual</strong>.</p>
            <p>Experimento: lente convergente pode projetar imagem da janela no papel
            (geralmente <strong>invertida</strong>); divergente não forma imagem nítida projetada.</p>

            <h3>4. Visão e ametropias</h3>
            <p><strong>Miopia</strong> — enxerga mal de longe; corrige com lente <strong>divergente</strong>
            (texto visto pela lente fica menor). <strong>Hipermetropia</strong> — dificuldade de perto;
            lente <strong>convergente</strong> (texto ampliado pela lente).</p>
            <p><strong>Astigmatismo</strong> — curvaturas diferentes na córnea; visão borrada perto e longe;
            exige lentes especiais. Não esfregar os olhos — deforma temporariamente a córnea.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Vidro de painel solar: parte da luz reflete e parte refrata — não é só um fenômeno.
            </div>""",
            "resumo": """
            <h3>Fontes de luz</h3>
            <table>
              <thead><tr><th>Tipo</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>Primária</td><td>Sol, vela</td></tr>
                <tr><td>Secundária</td><td>Lua, página do livro</td></tr>
              </tbody>
            </table>

            <h3>Fenômenos</h3>
            <p>Reflexão difusa · especular · absorção · dispersão · refração.</p>

            <h3>Lentes</h3>
            <p>Convergente (bordas finas, foco real) · divergente (bordas grossas, foco virtual).</p>

            <h3>Óculos</h3>
            <p>Miopia → divergente · hipermetropia → convergente.</p>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Confundir convergente com miopia é pegadinha — miopia usa lente divergente!
            </div>""",
            "dicas": """
            <ul>
              <li>Convergente = bordas finas; divergente = bordas grossas (desenho do caderno).</li>
              <li>Na prova do painel solar: reflexão <em>e</em> refração podem ocorrer juntas no vidro.</li>
              <li>Imagem pela lente convergente no papel costuma ser invertida em relação ao objeto.</li>
              <li>Texto maior pelo óculos = lente convergente (hipermetropia, no exemplo Helena/Pedro inverta conforme figura).</li>
              <li>Astigmatismo afeta foco em várias direções — não é só «de perto» ou «de longe».</li>
              <li>Propagação = movimento da luz no meio; sem meio transparente adequado, a imagem muda.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Corpos que emitem luz própria são chamados no caderno de fontes:",
                ["Secundárias apenas", "Primárias", "Extensas obrigatoriamente", "Virtuais"],
                1,
                "Primárias emitem luz; secundárias só refletem.",
                "Resposta correta: primárias.",
            ),
            _mc(
                "Leia as afirmativas sobre fenômenos ópticos:\n"
                "I. Reflexão difusa espalha a luz sem imagem nítida.\n"
                "II. Refração ocorre ao mudar de meio.\n"
                "III. Dispersão separa cores da luz branca.\n"
                "IV. Absorção faz a folha verde refletir principalmente verde.\n\n"
                "Estão corretas apenas:",
                ["I e II", "I, II e III", "I, II, III e IV", "III e IV"],
                2,
                "Todas corretas segundo o Módulo 25.",
                "Resposta correta: I, II, III e IV.",
            ),
            _mc(
                "Lentes de bordas finas são classificadas como:",
                ["Divergentes", "Convergentes", "Apenas espelhos", "Sem foco"],
                1,
                "Bordas finas → convergentes com foco real.",
                "Resposta correta: convergentes.",
            ),
            _mc(
                "Em lente divergente, raios paralelos ao eixo principal:",
                [
                    "Convergem a um foco real à direita",
                    "Divergem como se saíssem de um foco virtual",
                    "Não sofrem refração",
                    "Formam sempre imagem invertida no papel",
                ],
                1,
                "Divergente espalha os raios — foco virtual.",
                "Resposta correta: divergem a partir de foco virtual.",
            ),
            _mc(
                "No experimento com papel na parede, a lente convergente em geral projeta imagem:",
                ["Maior e sempre invertida", "Invertida (pode variar o tamanho conforme distância)", "Impossível de formar", "Idêntica sem inversão"],
                1,
                "Caderno pede descrever tamanho e orientação — convergente forma imagem real, em geral invertida.",
                "Resposta correta: invertida (tamanho depende da distância).",
            ),
            _mc(
                "Lente divergente, no mesmo experimento:",
                ["Projeta imagem nítida invertida", "Não projeta imagens níticas como a convergente", "Só funciona à noite", "Concentra raios no foco real"],
                1,
                "Conclusão do caderno: divergente não projeta imagens.",
                "Resposta correta: não projeta imagens níticas.",
            ),
            _mc(
                "Em painel solar, luz no vidro semitransparente:",
                [
                    "Só reflete totalmente",
                    "Pode refletir parcialmente e refratar parcialmente",
                    "Só dispersa, sem refração",
                    "Desaparece sem efeito",
                ],
                1,
                "Questão Uece do caderno — alternativa b.",
                "Resposta correta: parcialmente refletida e parcialmente refratada.",
            ),
            _mc(
                "Astigmatismo está relacionado principalmente a:",
                [
                    "Curvaturas diferentes da córnea em direções distintas",
                    "Excesso de luz solar apenas",
                    "Uso de lente divergente em ambos os olhos de hipermetros",
                    "Ausência total de retina",
                ],
                0,
                "Raios não convergem a um único ponto — visão borrada.",
                "Resposta correta: curvaturas diferentes da córnea.",
            ),
            _mc(
                "Se o texto visto pelas lentes do óculos fica menor que o texto ao redor, as lentes são:",
                ["Convergentes", "Divergentes", "Espelhos planos", "Primárias"],
                1,
                "Lente divergente diminui a imagem — típica de correção de miopia.",
                "Resposta correta: divergentes.",
            ),
            _mc(
                "Leia as afirmativas sobre óptica:\n"
                "I. Propagação é o deslocamento da luz no meio.\n"
                "II. Espelho plano forma imagem pelo fenômeno de reflexão.\n"
                "III. Toda refração gera dispersão visível em qualquer superfície.\n"
                "IV. Lente convergente pode associar-se à hipermetropia.\n\n"
                "Estão corretas apenas:",
                ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                1,
                "I, II e IV corretas. Dispersão não aparece sempre de forma visível (III exagerada).",
                "Resposta correta: I, II e IV.",
            ),
            _sa(
                "Cite um fenômeno óptico e um exemplo do cotidiano citado no caderno.",
                ["refração", "reflexão", "dispersão", "absorção", "gota", "folha"],
                "Qualquer par fenômeno + exemplo coerente do módulo.",
                "Exemplo: refração na gota d'água que funciona como lente.",
            ),
        ],
    }


def _subject_historia() -> dict:
    return {
        "title": "História",
        "icon": "HI",
        "sections": {
            "percurso": f"""
            <p><strong>Módulo 19 — Uma cultura de fé:</strong> arte religiosa medieval, poder da Igreja,
            mulheres na Idade Média. <strong>Módulo 20 — Cruzadas:</strong> motivações, Jerusalém,
            violência da conquista de 1099, consequências.</p>
            {PERCURSO_STEPS}""",
            "explicacao": """
            <h3>1. Cultura de fé (Módulo 19)</h3>
            <p>Pinturas medievais mostram o <strong>julgamento das almas</strong> (balança entre anjo e demônio).
            Esse tipo de imagem reforçava o medo do pecado e o <strong>poder de convencimento</strong> da
            Igreja Católica.</p>

            <h3>2. Igreja no cotidiano</h3>
            <p>Textos como o de <strong>São Elói</strong> (séc. VII) condenavam adivinhações, danças e cantos
            em festas — rotulados como «obras diabólicas». Chamar uma prática de diabólica significava
            forte repressão social e religiosa.</p>

            <h3>3. Mulheres na Europa antiga e medieval</h3>
            <p>Infográfico do caderno compara Atenas (mulheres no lar, sem cidadania plena), Esparta
            (exceção com treinamento e propriedade) e Roma (tutela masculina; mais espaço no Império, mas
            sem Senado). Na Idade Média, o cristianismo associou mulher a <strong>Maria</strong>
            (obediência) ou a <strong>Eva</strong> (tentação) — «não era fácil ser mulher».</p>

            <h3>4. Cruzadas — motivações (Módulo 20)</h3>
            <p>Além da fé: pressão turca em Bizâncio, falta de terra na Europa, interesse de nobres sem
            feudos, comerciantes italianos no Mediterrâneo, prestígio dos reis. <strong>Roberto, o Monge</strong>
            descreve Jerusalém como «umbigo do mundo» e pede libertação da cidade.</p>

            <h3>5. Conquista de Jerusalém (1099) e fontes</h3>
            <p>Relatos árabes (Amin Maalouf) e cristãos (Raimundo de Aguilers) descrevem violência extrema.
            Historiadores debatem responsabilidades. Consequências: reforço da ideia de «cristandade» na Europa,
            ressentimento no mundo árabe, <strong>comerciantes italianos</strong> entre os grandes beneficiados.</p>

            <div class="callout callout--remember">
              <strong>Lembre-se</strong>
              Jerusalém é sagrada para cristianismo, islamismo e judaísmo — não é exclusiva de uma fé.
            </div>""",
            "resumo": """
            <h3>Módulo 19</h3>
            <p>Arte do julgamento · Igreja no cotidiano · mulheres (Atenas/Esparta/Roma/Idade Média).</p>

            <h3>Módulo 20</h3>
            <p>Cruzadas = fé + política + comércio · 1099 · fontes em perspectivas diferentes.</p>

            <table>
              <thead><tr><th>Motivação</th><th>Exemplo</th></tr></thead>
              <tbody>
                <tr><td>Religiosa</td><td>Retomar Jerusalém</td></tr>
                <tr><td>Política/econômica</td><td>Terras, rotas, prestígio</td></tr>
              </tbody>
            </table>

            <div class="callout callout--attention">
              <strong>Atenção</strong>
              Afirmativa III do Enem: tolerância religiosa na idade das Cruzadas — falsa.
            </div>""",
            "dicas": """
            <ul>
              <li>Pinturas de julgamento ligam arte à autoridade da Igreja — leia o enunciado com calma.</li>
              <li>«Diabólica» no texto de São Elói = condenação forte, não piada.</li>
              <li>Esparta é a exceção grega para mulheres — contraste com Atenas cai na prova.</li>
              <li>Cruzadas: alternativa correta costuma unir fé + comércio, não «só política» ou «só comércio».</li>
              <li>Compare fontes cristãs e árabes — mesma guerra, narrativas diferentes.</li>
              <li>Beneficiários práticos: mercadores italianos, mesmo com Jerusalém mudando de mãos depois.</li>
            </ul>""",
        },
        "exercises": [
            _mc(
                "Pinturas medievais da «psicostasia» (balança das almas) serviam sobretudo para:",
                [
                    "Ensinar astronomia heliocêntrica",
                    "Reforçar crenças sobre julgamento e poder da Igreja",
                    "Substituir o latim nos mosteiros",
                    "Celebrar vitórias das Cruzadas apenas",
                ],
                1,
                "Arte religiosa convencia sobre destino da alma.",
                "Resposta correta: reforçar crenças e poder da Igreja.",
            ),
            _mc(
                "No discurso atribuído a São Elói, danças em festas de santos são condenadas como:",
                [
                    "Obras científicas",
                    "Obras diabólicas",
                    "Obras políticas neutras",
                    "Obras comerciais",
                ],
                1,
                "Fragmento do caderno — controle moral da Igreja.",
                "Resposta correta: obras diabólicas.",
            ),
            _mc(
                "Leia as afirmativas sobre mulheres:\n"
                "I. Em Atenas, mulheres eram associadas principalmente ao lar.\n"
                "II. Em Esparta, algumas elite exercitavam-se e geriam propriedades.\n"
                "III. Em Roma republicana, não havia tutela masculina.\n"
                "IV. Na Idade Média, Maria e Eva serviam de modelos opostos.\n\n"
                "Estão corretas apenas:",
                ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                1,
                "I, II e IV corretas. Tutela masculina existia em Roma (III falsa).",
                "Resposta correta: I, II e IV.",
            ),
            _mc(
                "O infográfico do caderno sugere que, na Idade Média, ser mulher era:",
                [
                    "Mais fácil que em Atenas em todos os aspectos",
                    "Difícil — cristianismo influenciou mentalidades",
                    "Idêntico à condição de senadoras romanas",
                    "Irrelevante para a Igreja",
                ],
                1,
                "Título: «não era fácil ser mulher».",
                "Resposta correta: difícil, com forte influência cristã.",
            ),
            _mc(
                "Sobre motivações das Cruzadas, o caderno destaca que:",
                [
                    "Foram exclusivamente comerciais",
                    "Uniram convicções religiosas e interesses (terras, comércio, poder)",
                    "Visavam apenas criar uma religião única sob o Papa",
                    "Não envolveram Jerusalém",
                ],
                1,
                "Alternativa c do teste p. 156.",
                "Resposta correta: fé + interesses materiais.",
            ),
            _mc(
                "Cristãos chamavam Jerusalém de «umbigo do mundo» porque:",
                [
                    "Era cidade sem importância religiosa",
                    "Era considerada centro simbólico sagrado",
                    "Ficava na América",
                    "Era capital do Império Romano do Oriente apenas",
                ],
                1,
                "Texto de Roberto, o Monge — cidade central na fé.",
                "Resposta correta: centro simbólico sagrado.",
            ),
            _mc(
                "Além da fé, nobres sem terras viam nas Cruzadas chance de:",
                [
                    "Estudar latim em mosteiros",
                    "Obter riqueza e terras",
                    "Abolir o feudalismo imediatamente",
                    "Fechar o Mediterrâneo",
                ],
                1,
                "«Outros interesses além da fé» — pillagem e feudos.",
                "Resposta correta: obter riqueza e terras.",
            ),
            _mc(
                "Segundo o caderno, consequência importante das Cruzadas foi:",
                [
                    "Decadência total do comércio italiano",
                    "Reabertura de rotas e contato entre Ocidente e Oriente",
                    "Fim imediato da violência religiosa",
                    "Centralização da justiça só nos camponeses",
                ],
                1,
                "Teste p. 156 — alternativa d.",
                "Resposta correta: rotas comerciais e contatos.",
            ),
            _mc(
                "Leia as afirmativas com base nas fontes sobre 1099:\n"
                "I. Textos cristãos e árabes descrevem grande violência.\n"
                "II. As narrativas são idênticas em todos os detalhes.\n"
                "III. Historiadores comparam perspectivas diferentes.\n"
                "IV. Mulheres e crianças aparecem como vítimas nos relatos.\n\n"
                "Estão corretas apenas:",
                ["I e II", "I, III e IV", "II e III", "I, II, III e IV"],
                1,
                "I, III e IV corretas. Perspectivas diferem (II falsa).",
                "Resposta correta: I, III e IV.",
            ),
            _mc(
                "Na questão Enem do caderno, a afirmativa sobre «respeito e tolerância religiosa» nas Cruzadas é:",
                ["Correta", "Incorreta", "Neutra", "Não abordada"],
                1,
                "III do Enem é falsa — conflitos foram violentos.",
                "Resposta correta: incorreta.",
            ),
            _sa(
                "Cite uma motivação religiosa e uma não religiosa das Cruzadas, conforme o Módulo 20.",
                ["jerusalém", "fé", "comércio", "terras", "bizâncio", "italianos"],
                "Fé retomar Terra Santa + política/comércio/terras.",
                "Exemplo: religiosa — libertar Jerusalém; não religiosa — rotas comerciais no Mediterrâneo.",
            ),
        ],
    }


def build_simulado() -> dict:
    return {
        "title": "Simulado da PI",
        "icon": "★",
        "intro": """Um teste com <strong>20 questões</strong> (10 por disciplina), todas de múltipla escolha,
              ligadas ao texto abaixo sobre o projeto <strong>«Luz e Fé»</strong> e ao conteúdo das abas.""",
        "textTitle": "Texto-base — Projeto escolar «Luz e Fé»",
        "text": """
            <p>No 3º trimestre, a turma do <strong>6º ano</strong> montou o projeto
            <strong>«Luz e Fé»</strong>. Em Ciências, um grupo explicou que a luz das velas na maquete
            de uma igreja medieval era fonte <strong>primária</strong>, enquanto as paredes iluminadas eram
            <strong>secundárias</strong>. Outro cartão mostrava <strong>vitrais</strong>: a luz branca
            sofria <strong>dispersão</strong> e <strong>refração</strong> no vidro colorido.</p>

            <p>Um painel sobre <strong>fenômenos ópticos</strong> comparava o brilho de uma gota (reflexão
            <strong>especular</strong>) com a cor verde de uma folha (reflexão <strong>difusa</strong> e
            <strong>absorção</strong> das outras cores). O professor lembrou que <strong>lentes convergentes</strong>
            (bordas finas) podem projetar no papel imagens <strong>invertidas</strong> da janela, ao passo que
            lentes <strong>divergentes</strong> não formam projeção nítida.</p>

            <p>Para falar de visão, Pedro colocou óculos sobre o caderno: pelas lentes o texto ficava
            <strong>menor</strong> — típico de lentes <strong>divergentes</strong> usadas na
            <strong>miopia</strong>. Helena usou lentes que <strong>ampliavam</strong> as letras, associadas
            à <strong>hipermetropia</strong>. Um vídeo citou o <strong>astigmatismo</strong>, quando a córnea
            tem curvaturas diferentes e a imagem não foca em um só ponto.</p>

            <p>No corredor de História, cartazes do <strong>Módulo 19</strong> reproduziam pinturas do
            <strong>julgamento das almas</strong> — anjo e demônio na balança — para discutir como a
            <strong>Igreja Católica</strong> orientava a mentalidade medieval. Um trecho de
            <strong>São Elói</strong> condenava danças «diabólicas» em festas religiosas.</p>

            <p>O infográfico <strong>«Na Europa antiga e medieval, não era fácil ser mulher»</strong>
            contrastava Atenas, Esparta e Roma. Na sequência, painéis do <strong>Módulo 20</strong> explicavam
            que as <strong>Cruzadas</strong> uniram fé (retomar <strong>Jerusalém</strong>, «umbigo do mundo»
            para cristãos) a interesses de <strong>comerciantes italianos</strong> e nobres em busca de
            <strong>terras</strong>. Fontes sobre <strong>1099</strong> mostravam violência descrita tanto
            por cronistas cristãos quanto por autores árabes.</p>""",
        "questions": [
            {
                "discipline": "Ciências",
                "question": "Na maquete, a chama da vela é exemplo de fonte:",
                "options": ["Secundária", "Primária", "Virtual", "Extensa obrigatoriamente"],
                "correctAnswer": 1,
                "explanation": "Emite luz própria — fonte primária.",
            },
            {
                "discipline": "Ciências",
                "question": "Vitrais coloridos ilustram principalmente:",
                "options": [
                    "Só reflexão difusa",
                    "Dispersão e refração da luz branca",
                    "Ausência de propagação",
                    "Foco virtual de espelhos",
                ],
                "correctAnswer": 1,
                "explanation": "Luz branca separa-se e muda de meio no vidro.",
            },
            {
                "discipline": "Ciências",
                "question": "Brilho na gota d'água é reflexão:",
                "options": ["Difusa", "Especular", "Inexistente", "Térmica"],
                "correctAnswer": 1,
                "explanation": "Superfície lisa forma brilho nítido.",
            },
            {
                "discipline": "Ciências",
                "question": "Folha verde vista como verde envolve sobretudo:",
                "options": [
                    "Absorção de outras cores e reflexão do verde",
                    "Emissão própria de luz azul",
                    "Foco virtual em divergentes",
                    "Tetraplegia na retina",
                ],
                "correctAnswer": 0,
                "explanation": "Pigmento reflete verde, absorve demais cores.",
            },
            {
                "discipline": "Ciências",
                "question": "Lente convergente no experimento da janela tende a formar imagem:",
                "options": ["Sempre direita", "Invertida no papel", "Impossível", "Sem refração"],
                "correctAnswer": 1,
                "explanation": "Projeto descreve imagens invertidas.",
            },
            {
                "discipline": "Ciências",
                "question": "Lentes divergentes, no mesmo experimento:",
                "options": [
                    "Não projetam imagem nítida",
                    "Sempre ampliam o objeto",
                    "Só funcionam com Sol",
                    "Têm foco real à direita",
                ],
                "correctAnswer": 0,
                "explanation": "Conclusão do módulo 26.",
            },
            {
                "discipline": "Ciências",
                "question": "Óculos de Pedro deixam o texto menor — são lentes:",
                "options": ["Convergentes de hipermetropia", "Divergentes de miopia", "Primárias", "De astigmatismo apenas"],
                "correctAnswer": 1,
                "explanation": "Texto menor = divergente; associado à miopia no texto.",
            },
            {
                "discipline": "Ciências",
                "question": "Helena amplia letras — associa-se a:",
                "options": ["Miopia e lente divergente", "Hipermetropia e lente convergente", "Astigmatismo sem correção", "Fonte secundária"],
                "correctAnswer": 1,
                "explanation": "Ampliação indica convergente — hipermetropia.",
            },
            {
                "discipline": "Ciências",
                "question": "Astigmatismo ocorre quando:",
                "options": [
                    "Córnea tem curvaturas diferentes",
                    "Não há propagação da luz",
                    "Jerusalém é conquistada",
                    "Só há reflexão especular",
                ],
                "correctAnswer": 0,
                "explanation": "Raios não convergem a um ponto único.",
            },
            {
                "discipline": "Ciências",
                "question": "Leia com base no texto do projeto:\n"
                "I. Fonte secundária reflete luz incidente.\n"
                "II. Propagação é o deslocamento da luz no meio.\n"
                "III. Toda lente divergente projeta imagem invertida nítida.\n"
                "IV. Fenômenos ópticos podem ocorrer juntos.\n\n"
                "Estão corretas apenas:",
                "options": ["I e III", "I, II e IV", "II e III", "I, II, III e IV"],
                "correctAnswer": 1,
                "explanation": "I, II e IV corretas. Divergente não projeta nítida (III falsa).",
            },
            {
                "discipline": "História",
                "question": "Pinturas do julgamento das almas reforçavam:",
                "options": [
                    "Teoria das lentes divergentes",
                    "Autoridade religiosa e medo do pecado",
                    "Rotas comerciais italianas",
                    "Astigmatismo",
                ],
                "correctAnswer": 1,
                "explanation": "Arte medieval convence sobre destino espiritual.",
            },
            {
                "discipline": "História",
                "question": "São Elói, no trecho do projeto, critica práticas consideradas:",
                "options": ["Científicas", "Diabólicas", "Republicanas", "Ópticas"],
                "correctAnswer": 1,
                "explanation": "Danças e cantos condenados como diabólicos.",
            },
            {
                "discipline": "História",
                "question": "No infográfico, Esparta se destaca porque algumas mulheres:",
                "options": [
                    "Eram senadoras",
                    "Treinavam e administravam propriedades",
                    "Não existiam na cidade",
                    "Proibiam o cristianismo",
                ],
                "correctAnswer": 1,
                "explanation": "Exceção em relação a Atenas.",
            },
            {
                "discipline": "História",
                "question": "«Não era fácil ser mulher» resume sobretudo:",
                "options": [
                    "Igualdade plena na Idade Média",
                    "Restrições sociais e influência da Igreja",
                    "Ausência de religião",
                    "Vitórias exclusivas de gladiadoras",
                ],
                "correctAnswer": 1,
                "explanation": "Comparativo Antiguidade + medieval.",
            },
            {
                "discipline": "História",
                "question": "Cruzadas, no Módulo 20, combinavam:",
                "options": [
                    "Só interesse comercial",
                    "Fé em Jerusalém e interesses políticos/econômicos",
                    "Apenas estudo de óptica",
                    "Paz religiosa garantida",
                ],
                "correctAnswer": 1,
                "explanation": "Texto do projeto cita fé + italianos + terras.",
            },
            {
                "discipline": "História",
                "question": "Jerusalém como «umbigo do mundo» expressa:",
                "options": [
                    "Irrelevância religiosa",
                    "Centralidade simbólica para cristãos",
                    "Localização na América",
                    "Teoria do foco real",
                ],
                "correctAnswer": 1,
                "explanation": "Motivação religiosa nas pregações.",
            },
            {
                "discipline": "História",
                "question": "Comerciantes italianos, segundo o caderno, foram:",
                "options": [
                    "Prejudicados para sempre",
                    "Entre os grandes beneficiados práticos",
                    "Ausentes do Mediterrâneo",
                    "Responsáveis pelo astigmatismo",
                ],
                "correctAnswer": 1,
                "explanation": "Rotas e comércio se intensificaram.",
            },
            {
                "discipline": "História",
                "question": "Relatos de 1099 mostram que:",
                "options": [
                    "Não houve violência",
                    "Fontes cristãs e árabes descrevem massacre",
                    "Só musulmanos escreveram crônicas",
                    "Jerusalém ficou sob bizantinos para sempre",
                ],
                "correctAnswer": 1,
                "explanation": "Perspectivas diferentes, mas violência presente.",
            },
            {
                "discipline": "História",
                "question": "Motivação de nobres sem terras incluía:",
                "options": [
                    "Buscar novas terras e riqueza",
                    "Estudar dispersão da luz",
                    "Abolir vitrais",
                    "Proibir comércio",
                ],
                "correctAnswer": 0,
                "explanation": "«Outros interesses além da fé».",
            },
            {
                "discipline": "História",
                "question": "Leia com base no texto:\n"
                "I. Cristandade na Europa se reforçou após as expedições.\n"
                "II. Ressentimento árabe aumentou.\n"
                "III. Conflitos foram resolvidos só por tolerância mútua.\n"
                "IV. Jerusalém permaneceu simbólica para várias religiões.\n\n"
                "Estão corretas apenas:",
                "options": ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correctAnswer": 1,
                "explanation": "I, II e IV corretas. III falsa (Enem do caderno).",
            },
        ],
    }