import re
from collections import Counter

# Load the transcript
transcript = """[Your transcript text here]"""

transcript = """
Hi Udemezue,
Thank you for the information provided.
No additional actions are required from your side regarding the change of residence address.
Best regards,
 
Lesya Maziy | Senior Immigration Consultant | People Advisory Services

EY Doradztwo Podatkowe Krupa Sp.k
Cell:519098065 | Lesya.Maziy@pl.ey.com 
Website: www.ey.com 



From: Udemezue Iloabachie <udemezue@gmail.com> 
Sent: Monday, November 17, 2025 10:54 AM
To: Lesya Syrnyk <Lesya.Maziy@pl.ey.com>
Cc: Citi Immigration PMO Mailbox <citi.immigrationpmo@uk.ey.com>; EY Citi Poland Immigration <citi.polandimmigration@pl.ey.com>
Subject: Re: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]

Hello Lesya,

Trust you had a pleasant weekend.

I will be signing a new rental agreement at 5pm today so once signed I'll update the address on the form to the new address before signing it.

Please let me know if there is anything else I need to do given the change in my residential address.

Thank you.

Regards,
Udemezue.

On Thu, 13 Nov 2025 at 17:14, Lesya Syrnyk <Lesya.Maziy@pl.ey.com> wrote:
Hi Udemezue,
Thank you for your email.
We confirm that there have been changes at the Immigration Office.
 
What has changed?
As of 7 November 2025, the appointment booking calendar in the Foreigners’ Portal (inPOL) has been disabled. This means it is no longer possible to schedule visits for submitting applications for:
•	Temporary stay
•	Permanent stay
•	EU long-term resident status
 
How can you submit your application now?
Until the new MOS system becomes operational (expected in January 2026), applications can only be submitted:
•	By post – this is the recommended option.
•	At the filing desk (“biuro podawcze”) – however, please note that arranging submission at the desk is very difficult or even impossible due to the heavy workload of the Immigration Office.
 
EY will send your application by registered mail on your behalf. We will also obtain:
•	Confirmation of postal dispatch (available approximately after 7 days)
•	Confirmation of receipt from the Immigration Office (available approximately after 4 weeks)
 
Both documents will be sent to you by email. Once you receive them, please upload them immediately to WorkDay.
 
Why is this important?
The confirmation of postal submission will serve as proof of your legal stay (after the expiry of your current visa/residence permit) until you receive a stamp in your passport during the biometric appointment.
 
What does the process look like now?
•	CAUTION:  At the day of sending the application via post and delivering the application to the Immigration Office, you are required to be present in Poland (usually, the application is delivered to the Immigration Office within 2 weeks, so it is important to inform us about any planned trips after sending the application). Please be advised that failing to meet this obligation will result in rejecting your application by the Immigration Office.
•	7–8 months after sending the application, you will receive an official letter requesting a personal visit to submit fingerprints, biometric photos, and original documents.
•	After this visit, the Immigration Office will analyze your case for 5–9 months before issuing a decision.
•	Once the decision is issued, your residence card will be prepared within 1,5-2 months.
Overall, currently the process may take approximately 14–19 months and could be extended at any time due to the high volume of applications and the workload of the Immigration Office.
 
We understand that these changes may cause inconvenience and uncertainty. Please be assured that we are here to support you throughout this process and will keep you informed of any developments.
 
Therefore, please find attached a draft of your application and the power of attorney, which must be signed by you so that we can submit the application to the Immigration Office. The password to open the file will be provided in a separate email.
Please print the attached documents in two copies and sign in the places marked with comments. Leave the originals of the signed documents in the Citi mailroom in an envelope addressed to me. As soon as we receive the signed documents from you, we will immediately send them to the Immigration Office.
 
Please also provide the information regarding your family members that is required in section C.II., so that we can complete this information accordingly.
 
If you have any questions or need assistance, please do not hesitate to contact us.
 
Best regards,
 
 
Lesya Maziy | Senior Immigration Consultant | People Advisory Services
 
EY Doradztwo Podatkowe Krupa Sp.k
Cell:519098065 | Lesya.Maziy@pl.ey.com 
Website: www.ey.com 

 
 
From: udemezue@gmail.com <udemezue@gmail.com> 
Sent: Wednesday, November 12, 2025 1:27 PM
To: Lesya Syrnyk <Lesya.Maziy@pl.ey.com>
Cc: Citi Immigration PMO Mailbox <citi.immigrationpmo@uk.ey.com>; EY Citi Poland Immigration <citi.polandimmigration@pl.ey.com>
Subject: RE: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Hello Lesya,
 
I got information that the booking portal has been disabled.  Please see the information below.
 
https://en.migrant.wsc.mazowieckie.pl/pl/komunikaty/wylaczony-kalendarz-rezerwacji-wizyt
 
Regards,
Udemezue.
 
 
From: Lesya Syrnyk <Lesya.Maziy@pl.ey.com> 
Sent: 06 November 2025 12:53
To: Udemezue Iloabachie <udemezue@gmail.com>
Cc: Citi Immigration PMO Mailbox <citi.immigrationpmo@uk.ey.com>; EY Citi Poland Immigration <citi.polandimmigration@pl.ey.com>
Subject: RE: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Hi Udemezue,
Of course, you can also try to book an appointment at the Immigration Office in parallel with us. Attached, I am sending a brief instruction on how to navigate the InPol website. You can also find the login details for your InPol account in the attachment (the password to open the file will be provided in a separate email).
Typically, the Immigration Office releases available slots around 8:00 or 9:00 AM.
Our support team will also try to book an appointment for you at the Immigration Office every day.
If you have any further questions, feel free to ask.
Best regards,
 
Lesya Maziy | Senior Immigration Consultant | People Advisory Services
 
EY Doradztwo Podatkowe Krupa Sp.k
Cell:519098065 | Lesya.Maziy@pl.ey.com 
Website: www.ey.com 

 
 
From: Udemezue Iloabachie <udemezue@gmail.com> 
Sent: Thursday, November 6, 2025 9:55 AM
To: Lesya Syrnyk <Lesya.Maziy@pl.ey.com>
Cc: Citi Immigration PMO Mailbox <citi.immigrationpmo@uk.ey.com>; EY Citi Poland Immigration <citi.polandimmigration@pl.ey.com>
Subject: Re: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Hello Lesya,
 
Is it something I can do?  Could you share the link to the appointment booking site?
 
Thank you.
 
Udemezue.
 
On Wed, 5 Nov 2025 at 15:26, Lesya Syrnyk <Lesya.Maziy@pl.ey.com> wrote:
Hi Udemezue,
Unfortunately, the Immigration Office system still hasn't been fixed. Nevertheless, we attempt to book an appointment for you every day.
Best regards,
 
Lesya Maziy | Senior Immigration Consultant | People Advisory Services
 
EY Doradztwo Podatkowe Krupa Sp.k
Cell:519098065 | Lesya.Maziy@pl.ey.com 
Website: www.ey.com 

 
 
From: Udemezue Iloabachie <udemezue@gmail.com> 
Sent: Wednesday, November 5, 2025 1:28 PM
To: Lesya Syrnyk <Lesya.Maziy@pl.ey.com>
Subject: Re: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Hello Lesya,
 
Trust you are doing great.
 
Could you confirm if you had any luck with my application?
 
Thank you.
 
Regards,
Udemezue Iloabachie.
 
On Tue, 28 Oct 2025 at 21:15, Lesya Maziy <Lesya.Maziy@pl.ey.com> wrote:
Hi Udemezue,
Thank you for your response.
Over the next month, we will continue our efforts to secure an appointment for you at the Immigration Office. Please rest assured that we are actively monitoring the system and will keep you informed of any progress or changes regarding the booking process.
Should you have any questions or require further assistance in the meantime, please do not hesitate to reach out.
Best regards,
 
Lesya Maziy | Senior Immigration Consultant | People Advisory Services
 
EY Doradztwo Podatkowe Krupa Sp.k
Cell:519098065 | Lesya.Maziy@pl.ey.com 
Website: www.ey.com 

 
 
From: udemezue@gmail.com <udemezue@gmail.com> 
Sent: Monday, October 27, 2025 10:45 PM
To: Lesya Maziy <Lesya.Maziy@pl.ey.com>
Cc: Citi Immigration PMO Mailbox <citi.immigrationpmo@uk.ey.com>; EY Citi Poland Immigration <citi.polandimmigration@pl.ey.com>; Immig Past2025sec <Immig.Past2025sec@pl.ey.com>
Subject: RE: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Hello Lesya,
 
Trust you are doing great.
 
Thank you for sharing the update with me.
 
I would say we can wait one more month and if there is still no success with the online booking system, then you may proceed with the mail in option without further checking with me.
 
Thank you.
 
Regards,
Udemezue.
 
From: Lesya Maziy <Lesya.Maziy@pl.ey.com> 
Sent: 24 October 2025 17:39
To: udemezue@gmail.com
Cc: Citi Immigration PMO Mailbox <citi.immigrationpmo@uk.ey.com>; EY Citi Poland Immigration <citi.polandimmigration@pl.ey.com>; Immig Past2025sec <Immig.Past2025sec@pl.ey.com>
Subject: RE: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Dear Udemezue,
I hope you are doing well!
I am here to provide you with a detailed overview of the current situation regarding the appointment at the Immigration Office.
The Warsaw Immigration Office's booking system refreshes daily, and available appointments appear between 8:00 and 10:00 each morning. However, in reality, the slots become available precisely at 9:00 and are usually exhausted around 9:05. This means that we do not have a full calendar to choose from, but rather just "the new" day that appears. For the past few weeks, we have been diligently trying to book an appointment for you every single day. Unfortunately, the website has not been showing us any available dates, or even when they do appear, the system fails to process our request, resulting in no appointment being set. To give you a clearer picture, over the last 30 days, twenty EY employees have been attempting to book appointments daily, and we have only managed to secure six slots. In the last two weeks, we booked none.
Unfortunately, we do not have information on when the personal appointment booking system will be restored to normal. EY is not alone in facing these challenges, and official complaints have been sent to the Authorities.
Due to the aforementioned issues, we would recommend submitting the application via post as we do not know when the system will start working again.
The timeline of the process will look as follows:
•	The average processing time of the residence permit application is around 11-12 months after the application is submitted, for applications sent by post – 16-18 months.
•	After sending the application (7-8 months from the day of sending application) we will receive an official letter from Immigration Office, with a request of personal visit to submit fingerprints, biometric photos and to present passport. During the visit we will be able to submit all other additional documents (when we receive the letter, we will notify you and send you a list of documents required from you in originals – we will bring set of copies to submit, but originals need to be presented to the officer at the same time)
•	Once fingerprints are submitted, we will receive the second letter, confirming status of your application with estimated date of decision issuance.
•	The Immigration Office will analyze the case for about 4-9 months.
•	During the visit you will also receive a stamp in passport, which is an additional confirmation of submitted application and legal stay in Poland after current residence permit expiration date
•	At the end of the process, your residence permit decision will be issued. After that, Residence Card will be issued within next 2-3 months from the date of decision issuance.
Please let me know if you agree to submit your Residence Permit application by post. Thank you for your understanding and patience as we navigate these challenges.
Best regards,
 
Lesya Maziy | Senior Immigration Consultant | People Advisory Services
 
EY Doradztwo Podatkowe Krupa Sp.k
Cell:519098065 | Lesya.Maziy@pl.ey.com 
Website: www.ey.com 

From: Magdalena Milkiewicz <Magdalena.Milkiewicz@pl.ey.com> 
Sent: Wednesday, October 22, 2025 12:55 PM
To: udemezue@gmail.com; Lesya Maziy <Lesya.Maziy@pl.ey.com>
Cc: Citi Immigration PMO Mailbox <citi.immigrationpmo@uk.ey.com>; EY Citi Poland Immigration <citi.polandimmigration@pl.ey.com>; Immig Past2025sec <Immig.Past2025sec@pl.ey.com>; Valeriia Herasymenko <Valeriia.Herasymenko@pl.ey.com>
Subject: RE: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Dear Udemezue,
 
By way of brief introduction, my name is Magdalena Milkiewicz, and I am a member of the EY Poland Immigration Team. I’m contacting you on behalf of Lesya Maziy who is currently on annual leave.
 
Thank you for your inquiry.
 
If you entered Poland using a national visa issued in your Nigerian passport, you should submit your application for a temporary residence permit as a Nigerian citizen, even if you have recently obtained Canadian citizenship. It is not possible to use 2 passports at the same time (the main document is the one showed at the border control). 
 
As I understand, the current basis for your legal stay in Poland is the national visa in your Nigerian passport, and this determines how your residence application should be processed. Obtaining another citizenship after entry does not affect the conditions of your current stay.
 
Kindly share your Canadian passport scan copy for our records, it might be useful for your future processes.
 
Pozdrawiam serdecznie / Best regards,
Magda
 
Upcoming out of office:
10.11.2025-14.11.2025 
(please note that all EY Poland offices will be closed on 10.11.2025 and 11.11.2025 is a national holiday)
	 
 
Magdalena Milkiewicz | Senior | People Advisory Services
 
EY Doradztwo Podatkowe Krupa sp. k.
Jana z Kolna 11, 80-864 Gdańsk, Poland
Cell:508316180 | Magdalena.Milkiewicz@pl.ey.com 
My pronouns are: she/her/hers
Website: www.ey.com 
________________________________________
From: Udemezue Iloabachie <udemezue@gmail.com>
Sent: Wednesday, October 22, 2025 12:05:02 PM (UTC+01:00) Sarajevo, Skopje, Warsaw, Zagreb
To: Valeriia Herasymenko <Valeriia.Herasymenko@pl.ey.com>; Lesya Maziy <Lesya.Maziy@pl.ey.com>
Subject: Re: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
Hello Valeriia, Lesya,
 
Trust you are doing great. 
 
I wanted to check in on my application for Karta Pobytu.
 
What would be the next steps and do I need to send you a copy of my Canadian passport to include in the application as I only picked it up a couple of weeks ago?
 
Thank you. 
 
Regards, 
Udemezue. 
 
Le mer. 3 sept. 2025, 12 h 14, Valeriia Herasymenko <Valeriia.Herasymenko@pl.ey.com> a écrit :
Hi Udemezue,
 
Thank you. Please expect an email from our Support Team soon.
Best Regards,
Valeriia Herasymenko | Senior Immigration Consultant | People Advisory Services
EY Doradztwo Podatkowe Krupa Sp.k
Cell: 572 002 876 | Valeriia.Herasymenko@pl.ey.com
 
From: Udemezue Iloabachie <udemezue@gmail.com> 
Sent: Wednesday, September 3, 2025 10:09 AM
To: Valeriia Herasymenko <Valeriia.Herasymenko@pl.ey.com>
Subject: Re: Pre-hire assessment completed | ILOABACHIE, Udemezue Chukwuemeka I CITI |IndividualID[11128]
 
Hello, 
 
My address is:
 
Wysockiego 20/165, 03-388 Warsaw
 
Thank you. 
 
Regards, 
Udemezue. 
 
Le mer. 3 sept. 2025, 09 h 48, Valeriia Herasymenko <Valeriia.Herasymenko@pl.ey.com> a écrit :
Dear Udemezue,
I’m contacting you on behalf of @Lesya Maziy who is currently on annual leave. 
Could you please provide us with your place of residence in Poland? The address is required for ZUS and TAX applications we are going to obtain on your behalf.
 
 
 
Best Regards,
Valeriia Herasymenko | Senior Immigration Consultant | People Advisory Services
 
EY Doradztwo Podatkowe Krupa Sp.k
Rondo ONZ 1, 00-124 , Warsaw, Poland
Cell: 572 002 876 | Valeriia.Herasymenko@pl.ey.com 
Website: www.ey.com 
 
 
 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

Odwiedź nasze strony:http://www.ey.com/pl. Informacje dot. przetwarzania danych osobowych uzyskasz TUTAJ. Treść tej wiadomości jest poufna i objęta zakazem ujawniania. Jeśli otrzymałaś/eś tą wiadomość omyłkowo, niezwłocznie zawiadom o tym nadawcę i usuń wiadomość z poczty. Rozprowadzanie, dystrybucja lub powielanie tej wiadomości przez osoby, które nie są jej adresatami, są zabronione. || Visit us on the Web at http://www.ey.com/poland. Information on processing of personal data you receive HERE. This message is confidential and protected from disclosure. If you received this message by mistake you should immediately notify the sender and delete the message from your computer. Any dissemination, distribution or copying of this communication by unintended users is strictly prohibited. 

"""

# Basic text analysis functions
def count_words(text):
    """Count total words in the text"""
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)

def most_common_words(text, n=10):
    """Find the most common words (excluding common stop words)"""
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                  'of', 'with', 'is', 'was', 'are', 'were', 'be', 'been', 'have', 'has',
                  'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'it',
                  'that', 'this', 'as', 'by', 'from', 'they', 'we', 'you', 'i'}
    
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
    return Counter(filtered_words).most_common(n)

def find_speakers(text):
    """Extract speaker changes (marked by >>)"""
    speakers = re.findall(r'>>\s*([^>]+?)(?=\n|>>)', text)
    return len(speakers)

def extract_key_topics(text):
    """Extract main topics mentioned"""
    topics = {
        'public media': len(re.findall(r'public media|public broadcasting|PBS|NPR', text, re.I)),
        'CPB': len(re.findall(r'\bCPB\b', text, re.I)),
        'funding': len(re.findall(r'funding|budget|money|dollars', text, re.I)),
        'stations': len(re.findall(r'station|stations', text, re.I)),
        'Bob Ross': len(re.findall(r'Bob Ross|Peepod', text, re.I))
    }
    return topics

# Analysis
print("=== Transcript Analysis ===\n")
print(f"Total words: {count_words(transcript):,}")
print(f"\nNumber of speaker segments: {find_speakers(transcript)}")

print("\n=== Most Common Words ===")
for word, count in most_common_words(transcript, 15):
    print(f"{word}: {count}")

print("\n=== Key Topics Mentioned ===")
topics = extract_key_topics(transcript)
for topic, count in sorted(topics.items(), key=lambda x: x, reverse=True):
    print(f"{topic}: {count} times")

# Extract auction items
print("\n=== Auction Items Mentioned ===")
auction_items = re.findall(r'(?:item|auctioning|auction)[^.]*?([A-Z][^.]+?(?:jockstrap|cabbage|balls|bedet|painting|sneakers|DVD))', transcript, re.I)
for item in set(auction_items):
    print(f"- {item.strip()}")