import requests, uuid, time, json, random, random_address
from requests_toolbelt import MultipartEncoder
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup as soup
from collections import OrderedDict
import cloudscraper

proxyList = []

def loadProxies():
    proxies = open('proxies.txt').read().splitlines()
    for proxy in proxies:
        try:
            if len(proxy.split(":")) == 2:
                ip = proxy.split(":")[0]
                port = proxy.split(":")[1]
                proxyData = {'http': 'http://{}:{}'.format(ip, port), 'https': 'http://{}:{}'.format(ip, port)}
                proxyList.append(proxyData)
            else:
                ip = proxy.split(":")[0]
                port = proxy.split(":")[1]
                user = proxy.split(":")[2]
                password = proxy.split(":")[3]
                proxyData = {'http': 'http://{}:{}@{}:{}'.format(user, password, ip, port), 'https': 'http://{}:{}@{}:{}'.format(user, password, ip, port)}
                proxyList.append(proxyData)
        except:
            pass

try:
    loadProxies()
except:
    pass

def multi_run_wrapper(args):
   return entering(*args)

def entering(firstName, lastName, email):
    getAddress = False
    while getAddress == False:
        try:
            listState = ["CT", "MA", "VT", "AL", "AR", "DC", "FL", "GA", "KY", "MD", "OK", "TN", "TX", "AK", "AZ", "CA", "CO", "HI"]
            stateSelected = random.choice(listState)
            addressCheckout = random_address.real_random_address_by_state(stateSelected)

            address = addressCheckout["address1"]
            #zipCode = addressCheckout["postalCode"]
            #address2 = addressCheckout["address2"]
            getAddress = True
        except Exception as e:
            continue
    fullName = firstName + " " + lastName
    listZip = ['90001', '90002', '90003', '90004', '90005', '90006', '90007', '90008', '90009', '90010', '90011', '90012', '90013', '90014', '90015', '90016', '90017', '90018', '90019', '90020', '90021', '90022', '90023', '90024', '90025', '90026', '90027', '90028', '90029', '90030', '90031', '90032', '90033', '90034', '90035', '90036', '90037', '90038', '90039', '90040', '90041', '90042', '90043', '90044', '90045', '90046', '90047', '90048', '90049', '90050', '90051', '90052', '90053', '90054', '90055', '90056', '90057', '90058', '90059', '90060', '90061', '90062', '90063', '90064', '90065', '90066', '90067', '90068', '90069', '90070', '90071', '90072', '90073', '90074', '90075', '90076', '90077', '90078', '90079', '90080', '90081', '90082', '90083', '90084', '90086', '90087', '90088', '90089', '90090', '90091', '90093', '90094', '90095', '90096', '90099', '90189', '90201', '90202', '90209', '90210', '90211', '90212', '90213', '90220', '90221', '90222', '90223', '90224', '90230', '90231', '90232', '90233', '90239', '90240', '90241', '90242', '90245', '90247', '90248', '90249', '90250', '90251', '90254', '90255', '90260', '90261', '90262', '90263', '90264', '90265', '90266', '90267', '90270', '90272', '90274', '90275', '90277', '90278', '90280', '90290', '90291', '90292', '90293', '90294', '90295', '90296', '90301', '90302', '90303', '90304', '90305', '90306', '90307', '90308', '90309', '90310', '90311', '90312', '90401', '90402', '90403', '90404', '90405', '90406', '90407', '90408', '90409', '90410', '90411', '90501', '90502', '90503', '90504', '90505', '90506', '90507', '90508', '90509', '90510', '90601', '90602', '90603', '90604', '90605', '90606', '90607', '90608', '90609', '90610', '90637', '90638', '90639', '90640', '90650', '90651', '90652', '90660', '90661', '90662', '90670', '90671', '90701', '90702', '90703', '90704', '90706', '90707', '90710', '90711', '90712', '90713', '90714', '90715', '90716', '90717', '90723', '90731', '90732', '90733', '90734', '90744', '90745', '90746', '90747', '90748', '90749', '90755', '90801', '90802', '90803', '90804', '90805', '90806', '90807', '90808', '90809', '90810', '90813', '90814', '90815', '90822', '90831', '90832', '90833', '90834', '90835', '90840', '90842', '90844', '90846', '90847', '90848', '90853', '90895', '90899', '91001', '91003', '91006', '91007', '91008', '91009', '91010', '91011', '91012', '91016', '91017', '91020', '91021', '91023', '91024', '91025', '91030', '91031', '91040', '91041', '91042', '91043', '91046', '91066', '91077', '91101', '91102', '91103', '91104', '91105', '91106', '91107', '91108', '91109', '91110', '91114', '91115', '91116', '91117', '91118', '91121', '91123', '91124', '91125', '91126', '91129', '91182', '91184', '91185', '91188', '91189', '91199', '91201', '91202', '91203', '91204', '91205', '91206', '91207', '91208', '91209', '91210', '91214', '91221', '91222', '91224', '91225', '91226', '91301', '91302', '91303', '91304', '91305', '91306', '91307', '91308', '91309', '91310', '91311', '91313', '91316', '91321', '91322', '91324', '91325', '91326', '91327', '91328', '91329', '91330', '91331', '91333', '91334', '91335', '91337', '91340', '91341', '91342', '91343', '91344', '91345', '91346', '91350', '91351', '91352', '91353', '91354', '91355', '91356', '91357', '91364', '91365', '91367', '91371', '91372', '91376', '91380', '91381', '91382', '91383', '91384', '91385', '91386', '91387', '91390', '91392', '91393', '91394', '91395', '91396', '91401', '91402', '91403', '91404', '91405', '91406', '91407', '91408', '91409', '91410', '91411', '91412', '91413', '91416', '91423', '91426', '91436', '91470', '91482', '91495', '91496', '91499', '91501', '91502', '91503', '91504', '91505', '91506', '91507', '91508', '91510', '91521', '91522', '91523', '91526', '91601', '91602', '91603', '91604', '91605', '91606', '91607', '91608', '91609', '91610', '91611', '91612', '91614', '91615', '91616', '91617', '91618', '91702', '91706', '91711', '91714', '91715', '91716', '91722', '91723', '91724', '91731', '91732', '91733', '91734', '91735', '91740', '91741', '91744', '91745', '91746', '91747', '91748', '91749', '91750', '91754', '91755', '91756', '91765', '91766', '91767', '91768', '91769', '91770', '91771', '91772', '91773', '91775', '91776', '91778', '91780', '91788', '91789', '91790', '91791', '91792', '91793', '91801', '91802', '91803', '91804', '91896', '91899', '93510', '93532', '93534', '93535', '93536', '93539', '93543', '93544', '93550', '93551', '93552', '93553', '93563', '93584', '93586', '93590', '93591', '93599']
    zipCode = random.choice(listZip)
    entered = False
    while entered == False:
        try:
            session = cloudscraper.create_scraper()
            if len(proxyList) != 0:
                session.proxies = random.choice(proxyList)
            url = "https://losangeles.doverstreetmarket.com/new-items/raffle"
            session.headers = OrderedDict([
                ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'),
                ('Accept-Encoding', 'gzip, deflate, br'),
                ('Accept-Language', 'en-GB,en-US;q=0.9,en;q=0.8'),
                ('Cache-Control', 'max-age=0'),
                ('Content-Type', 'application/x-www-form-urlencoded'),
                ('Origin', 'https://losangeles.doverstreetmarket.com'),
                ('Referer', url),
                ('Sec-Ch-Ua', '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"'),
                ('Sec-Ch-Ua-Mobile', '?0'),
                ('Sec-Ch-Ua-Platform', '"macOS"'),
                ('Sec-Fetch-Dest', 'document'),
                ('Sec-Fetch-Mode', 'navigate'),
                ('Sec-Fetch-Site', 'cross-site'),
                ('Sec-Fetch-User', '?1'),
                ('Upgrade-Insecure-Requests', '1'),
                ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
            ])
            timeOut = False
            while timeOut == False:
                try:
                    data = session.get(url, timeout=10)
                    timeOut = True
                except Exception as e:
                    if len(proxyList) != 0:
                        session.proxies = random.choice(proxyList)
            formContainer = soup(data.text, 'html.parser')
            listScripts = formContainer.findAll('link', {'rel': 'alternate stylesheet'})
            for each in listScripts:
                if 'www.tfaforms.com/dist/form-builder/' in str(each) and 'jsonly' in str(each):
                    url = each['href']
            timeOut = False
            while timeOut == False:
                try:
                    data = session.get(url, timeout=10)
                    timeOut = True
                except Exception as e:
                    if len(proxyList) != 0:
                        session.proxies = random.choice(proxyList)
            sizeList = []
            listSize = formContainer.find('select', {'name':'tfa_17'}).findAll('option')
            for each in listSize:
                if "US " in str(each):
                    sizeList.append(each['value'])
                
            formID = formContainer.find('input', {'name':'tfa_dbFormId'})['value']
            dbControl = formContainer.find('input', {'name':'tfa_dbControl'})['value']
            formVersion = formContainer.find('input', {'name':'tfa_dbVersionId'})['value']
            responseID = formContainer.find('input', {'name':'tfa_dbResponseId'})['value']
            sessionUUID = formContainer.find('input', {'name':'tfa_dbWorkflowSessionUuid'})['value']
            switchOff = formContainer.find('input', {'name':'tfa_switchedoff'})['value']
            if len(proxyList) != 0:
                session.proxies = random.choice(proxyList)
            url = "https://www.tfaforms.com/api_v2/workflow/processor"

            size = random.choice(sizeList)

            #colorList = ["tfa_78", "tfa_79"]
            #color = random.choice(colorList)

            payload = {
                "tfa_1": fullName,
                "tfa_9": str(random.randint(2000000000,9999999999)),
                "tfa_2": email,
                "tfa_11": address,
                "tfa_15": zipCode,
                "tfa_17": size, #Sizing tfa_40 tfa_42 tfa_23 tfa_25 tfa_27 tfa_29 tfa_31 tfa_33 tfa_35
                #"tfa_62": color, #Color tfa_78 tfa_79
                "tfa_6": "tfa_6",
                "tfa_dbFormId": formID,
                "tfa_dbResponseId": responseID,
                "tfa_dbControl": dbControl,
                "tfa_dbWorkflowSessionUuid": sessionUUID,
                "tfa_dbVersionId": formVersion,
                "tfa_switchedoff": switchOff
            }
            hasEntered = False
            timeOut = False
            while timeOut == False:
                try:
                    data = session.post(url, data=payload, timeout=10)
                    print(data)
                    if "thank_you" in str(data.url):
                        hasEntered = True
                    timeOut = True
                except Exception as e:
                    if len(proxyList) != 0:
                        session.proxies = random.choice(proxyList)
            
            if hasEntered == True:
                with open('Entered-dsmla.txt', 'a') as f:
                    data2save = email + ":" + str(size) + ":" + color
                    print(data2save)
                    f.write(data2save)
                    f.write('\n')
            entered = True
        except Exception as e:
            continue

profilesfull = []

profiles = open('dsmla.txt').read().splitlines()
for profile in profiles:
    string = profile.split(':')
    firstName = string[1]
    lastName = string[2]
    email = string[0]
    profilesfull.append({"firstName": firstName, "lastName": lastName, "email": email})

profilesentered = []

profiles = open('Entered-dsmla.txt').read().splitlines()
for profile in profiles:
    string = profile.split(':')
    email = string[0]
    try:
        size = string[1]
    except Exception as e:
        size = "None"
    try:
        color = string[2]
    except Exception as e:
        color = "None"
    profilesentered.append({"email": email, "size": size, "color": color})

profiles2enter = []

for item in profilesfull:
    if item['email'] not in [x['email'] for x in profilesentered]:
        firstName = item["firstName"]
        lastName = item["lastName"]
        email = item["email"]
        profiles2enter.append((firstName, lastName, email))

pool = ThreadPool(120)

while True:
    print("Starting")
    results = pool.map(multi_run_wrapper, profiles2enter)
    pool.close()
    pool.join()
    print(results)
