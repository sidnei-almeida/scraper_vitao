import requests
from bs4 import BeautifulSoup
import json
import time
import os
from urllib.parse import urljoin

class VitaoUrlCollector:
    def __init__(self):
        self.base_url = "https://www.fatsecret.com.br"
        self.search_url = "https://www.fatsecret.com.br/calorias-nutri%C3%A7%C3%A3o/search?q=Vitao"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.output_file = "dados/vitao_urls.json"
        self.collected_urls = []
        
    def get_page_content(self, url):
        """Faz a requisição HTTP e retorna o conteúdo da página"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            return None
    
    def extract_urls_from_page(self, soup):
        """Extrai URLs dos produtos da página atual"""
        urls = []
        
        # Busca por links com classe 'prominent' que são os produtos
        product_links = soup.find_all('a', class_='prominent')
        
        for link in product_links:
            href = link.get('href')
            if href and '/calorias-nutri%C3%A7%C3%A3o/vitao/' in href:
                # Constrói a URL completa
                full_url = urljoin(self.base_url, href)
                urls.append(full_url)
                print(f"  ✓ Encontrada: {link.get_text(strip=True)}")
        
        return urls
    
    def check_no_results(self, soup):
        """Verifica se a página não tem resultados"""
        no_results = soup.find('div', class_='searchNoResult')
        return no_results is not None
    
    def collect_all_urls(self):
        """Coleta todas as URLs dos produtos da Vitao"""
        print("🔍 Iniciando coleta de URLs dos produtos da Vitao...")
        
        page = 0
        total_urls = 0
        
        while True:
            # Constrói a URL da página
            if page == 0:
                page_url = self.search_url
            else:
                page_url = f"{self.search_url}&pg={page}"
            
            print(f"\n📄 Processando página {page + 1}...")
            print(f"URL: {page_url}")
            
            # Obtém o conteúdo da página
            content = self.get_page_content(page_url)
            if not content:
                print("❌ Erro ao acessar a página")
                break
            
            # Parse do HTML
            soup = BeautifulSoup(content, 'html.parser')
            
            # Verifica se não há resultados
            if self.check_no_results(soup):
                print("🏁 Nenhum resultado encontrado. Coleta finalizada.")
                break
            
            # Extrai URLs da página atual
            page_urls = self.extract_urls_from_page(soup)
            
            if not page_urls:
                print("⚠️  Nenhuma URL encontrada nesta página")
                break
            
            # Adiciona URLs à lista
            self.collected_urls.extend(page_urls)
            total_urls += len(page_urls)
            
            print(f"✅ {len(page_urls)} URLs coletadas da página {page + 1}")
            print(f"📊 Total acumulado: {total_urls} URLs")
            
            # Pausa entre requisições
            time.sleep(2)
            
            # Avança para a próxima página
            page += 1
        
        print(f"\n🎉 Coleta finalizada! Total de {len(self.collected_urls)} URLs coletadas.")
        return self.collected_urls
    
    def save_urls_to_json(self):
        """Salva as URLs coletadas em um arquivo JSON"""
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        
        # Remove URLs duplicadas
        unique_urls = list(set(self.collected_urls))
        
        # Salva no arquivo JSON
        with open(self.output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(unique_urls, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"💾 URLs salvas em: {self.output_file}")
        print(f"📝 {len(unique_urls)} URLs únicas salvas")
        
        return unique_urls
    
    def run(self):
        """Executa o processo completo de coleta"""
        # Coleta todas as URLs
        self.collect_all_urls()
        
        if self.collected_urls:
            # Salva no arquivo JSON
            unique_urls = self.save_urls_to_json()
            
            # Mostra algumas URLs como exemplo
            print("\n📋 Exemplos de URLs coletadas:")
            for i, url in enumerate(unique_urls[:5], 1):
                print(f"  {i}. {url}")
            
            if len(unique_urls) > 5:
                print(f"  ... e mais {len(unique_urls) - 5} URLs")
        else:
            print("❌ Nenhuma URL foi coletada")

def main():
    """Função principal"""
    collector = VitaoUrlCollector()
    collector.run()

if __name__ == "__main__":
    main() 