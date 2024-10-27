import pandas as pd
import openai


class generate:
    def __init__(self):
        self.api_key = open("APIkey.txt", "r").read().strip()  # Read and strip the API key

    def parse_and_fill_dataframe(self, output_text):

        # Define the columns of the dataframe
        columns = ['question', 'option1', 'reason1', 'option2', 'reason2', 'option3', 'reason3', 'option4', 'reason4']

        # Create an empty dataframe with the specified columns
        df = pd.DataFrame(columns=columns)

        try:
            options = []
            reasons = []
            questions = output_text.split("\n")
            question_text = questions[0].split(":")[1].strip()
            print(f"question text: {question_text}")
            for question in questions[1:]:
                if "Alternativ" in question:
                    line = question.split("#")
                    option = line[0].split(":")[1]
                    reason = line[1].split(":")[1]
                    options.append(option)
                    reasons.append(reason)

                
            # Fill in the dataframe (assuming each question has exactly 4 options)
            df.loc[len(df)] = [
                    question_text, 
                    options[0], reasons[0],
                    options[1], reasons[1],
                    options[2], reasons[2],
                    options[3], reasons[3]
                ]
            print("Question added to the dataframe")
            
        except (ValueError, IndexError):
            print("Error in parsing the output text")
            pass

    def generate_questions_from_text(self, page_text):
        prompt = f"""
        Du skal generere et flervalgsspørsmål basert på følgende utdrag fra boken:
        {page_text}
        
        Vennligst generer et flervalgsspørsmål med fire svaralternativer. For hvert alternativ, der alternativ 1 alltid skal være rett gi en forklaring på hvorfor svaret er korrekt eller feil. Formatér svaret som følger:

        du skal først skrive spørsmålet, etterulgt av :
        dereter skriver du svaralternativene etterfulgt av :, svaralternativet skal skrives først, så kommer : så kommer grunn til korrekthet eller feilaktighet.
        Du skal ikke bruke noen andre spesialtegn en ':'

        Spørsmål: spørsmålet
        Alternativ 1: alternativet # Grunnen til korrekthet: grunnen til korrekthet\n
        Alternativ 2: alternativet # Grunnen til feilaktighet: grunnen til feilaktighet\n
        Alternativ 3: alternativet # Grunnen til feilaktighet: grunnen til feilaktighet\n
        Alternativ 4: alternativet # Grunnen til feilaktighet: grunnen til feilaktighet\n
        """

        client = openai(api_key=self.api_key)
            
        response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "Du skal generere flervalgsspørsmål fra boken Tenk, det er viktig at du husker at spørsmålet du lager må kunne svares på ved kun å se på spørsmålet, du må derfor ikke referere til boken når du lager spørsmål, da de spm tar testen ike vil ha tilgang til boken. boken tenk er en bok for studenter i faget filosofi. du skal derfor lage spørsmål om ting du finner i boken innen kunnskaps- og vitenskapsteori, etikk og politisk filosofi. Ulike syn på natur, menneske og teknologi, i tillegg til spørsmål om relasjonen mellom individ og samfunn. spørsmålene du lager bør i en viss grad være relatert til et av følgende komptenasemål:\nanalyse og vurdering av argumentasjon, samt om sentrale begreper fra argumentasjonsteori sentrale teorier om viten, og hva som avgrenser vitenskapelig kunnskap fra andre kunnskapsformer\nutvalgte vitenskapsteoretiske temaer av spesiell relevans for matematisk-naturvitenskapelige fag og teknologi\nbærekraft som premiss for et godt samfunn i dag og i fremtiden, samt vitenskapens og teknologiens rolle i denne sammenhengen\nulike teorier og perspektiv på menneske, kultur og natur\nulike syn på forholdet mellom individ og fellesskap, samt organiseringen av samfunnet\nhovedtyper av etisk tenkning\netiske og samfunnsmessige problemstillinger relatert til naturvitenskapelig forskning og teknologiutvikling, herunder temaer innen forskningsetikk og forskningspolitikk, om du ikke kommer på noen spørsmål kan du svare med none"
                        },
                        {
                            "role": "system",
                            "content": "Det er viktig at du husker at den som skal svare ikke har tilgang til boken under testen men de har forberedt seg på kompetansemålene og lest om temaene i faget exphil, du skal derfor ikke lage spørsmål som fks: hva sier person x om klimakrisen, de eneste gangene du skal ha spørsmål om personer er dersom det er noen teoretikere innen fks filosofi. Du skal heller ikke lage noe spørsmål som fks: Hva sier teksten om ..., da den som skal svare har ikke tilgang til å lese teksten. Du skal heller ikke lage spørsmål om saker som fks hva sier person xx om klimakrisen, da dette ikke er noe som er nevt i kompetansemålene å gjøre: \nanalyse og vurdering av argumentasjon, samt om sentrale begreper fra argumentasjonsteori sentrale teorier om viten, og hva som avgrenser vitenskapelig kunnskap fra andre kunnskapsformer\nutvalgte vitenskapsteoretiske temaer av spesiell relevans for matematisk-naturvitenskapelige fag og teknologi\nbærekraft som premiss for et godt samfunn i dag og i fremtiden, samt vitenskapens og teknologiens rolle i denne sammenhengen\nulike teorier og perspektiv på menneske, kultur og natur\nulike syn på forholdet mellom individ og fellesskap, samt organiseringen av samfunnet\nhovedtyper av etisk tenkning\netiske og samfunnsmessige problemstillinger relatert til naturvitenskapelig forskning og teknologiutvikling, herunder temaer innen forskningsetikk og forskningspolitikk "
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="gpt-4o",
                )
        print(response.choices[0].message.content)
        return response.choices[0].message.content