import os, re, requests, bleach
def remove_pictured(r):
  remove_list = ['pictured', 'shown', 'highlighted']
  for to_remove in remove_list:
      pos = r.find(to_remove)
      if pos < 0: continue
      l = len(r)
      while pos < l:
          if r[pos] == ')':
              break
          pos += 1
      if pos >= l: continue
      end = pos
      close = 0
      start = -1
      while pos >= 0:
          if r[pos] == ')':
              close += 1
          elif r[pos] == '(':
              close -= 1
          if close == 0:
              start = pos
              break
          pos -= 1
      if start >= 0 and end >= 0:
          r = r[0:max(start, 0)] + r[1+end:]
  r = r.replace(' <i></i>', '').replace('<i></i>', '').replace('  ', ' ').replace(' .', '.').replace(' ,', ',')
  return r

def process_content():
  r = requests.get('https://en.wikipedia.org/wiki/Portal:Current_events').text
  r = r.split('id="Topics_in_the_news"', 1)[1].split('<ul>', 1)[1].split('</ul>', 1)[0]
  r = ' '.join(r.splitlines())
  ab = bleach.clean(r, attributes = {'a': ['href', 'title']}, strip=True)

  if ab != r:
    print('content change after bleach!')
    print('before:')
    print(r)
    print('after:')
    print(ab)

  r = '<ul>' + ab + '</ul>'
  r = r.replace("'", r"\'")
  ar = r 
  ar = remove_pictured(ar)
  
  if ar != r:
    print('content change after removing picture text:')
    print('before:')
    print(r)
    print('after:')
    print(ar)          

  ar = ar.replace("<li>", "\n<li>").replace("</ul>", "\n</ul>")
  r = "const content = `" + ar.replace('`', '\\`') + "`;"

  env_file = os.getenv('GITHUB_ENV')

  with open('content.js') as f: 
    s = f.read().strip()
    print('current file content:')
    print(s)
    print('fetched content:')
    print(r)
    
    if s == r:
      print('no content change')
      with open(env_file, 'a') as f:
        f.write("CHANGE=false\n")
    else:
      print('content change')
      with open('tmp_content.js', 'w') as tmp_file:
        tmp_file.write(r)
      with open(env_file, 'a') as f:
        f.write("CHANGE=true\n")

if __name__ == '__main__':
  process_content()
