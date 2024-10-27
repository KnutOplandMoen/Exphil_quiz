import re

def replace_delimiter(text):
    # Using regex to replace the delimiter only between content parts, not inside the text
    # The regex looks for ; that are not surrounded by quotes
    updated_text = re.sub(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', ',', text)
    return updated_text

# Original text
data = """
question;option1;reason1;option2;reason2;option3;reason3;option4;reason4
"I et leserbrev i en avis svarer en student på kritikk en universitetsprofessor har fremsatt i en kronikk. Kritikken fra professoren går på studenters bruk av sosiale medier. «De er ikke bare forstyrrende for undervisningen; de er også ødeleggende for studenters sosiale engasjement. For de forhindrer dem i å danne reelle sosiale nettverk»; hevder professoren. Studenten svarer at sosiale medier kan være et problem for eldre brukere som ikke er vokst opp med en slik teknologi. Men unge mennesker som har brukt dem siden de var små er «digitalt innfødte». Derfor har de langt bedre forutsetninger for å bruke dem på en positiv måte.Med utgangspunkt i filosofen Bernard Stiegler;"" hvilke argumenter kunne man brukt som støtte for studenten?; Teknologier former mye av det vi tenker på som menneskelig da de muliggjør vår kultur. Vennskap og sosiale nettverk er knyttet til kultur og vi har grunn til å anta at sosiale teknologier""; når vi først lærer å mestre dem;"" vil ha positiv innvirkning på dem. D;de andre er for generelle til at en filosof ville ha funnet de på.; Mennesket er et vesen som kompenserer for begrensede naturlige evner gjennom utvikling av ny teknologi. Slik teknologi kan veie opp for manglende evner til f.eks. å kommunisere meningsfylt med en større krets av mennesker.B;; Det er feil å hevde at en teknologi i seg selv er negativ""; da all teknologi i utgangspunktet er nøytral.Det er kun vår individuelle bruk av teknologiske midler som kan vurderes som positiv eller negativ. (Nøytralitetsargumentet og teknologi;"" skytevåpen;; Teknologier former mye av det vi tenker på som menneskelig da de muliggjør vår kultur. Vennskap og sosiale nettverk er knyttet til kultur og vi har grunn til å anta at sosiale teknologier""; når vi først lærer å mestre dem;"" vil ha positiv innvirkning på dem. D;"
"""

# Replace delimiters
updated_data = replace_delimiter(data)

# Print the updated data
print(updated_data)

# Optionally, write to a file
with open("updated_questions.csv", "w", encoding="utf-8") as file:
    file.write(updated_data)
