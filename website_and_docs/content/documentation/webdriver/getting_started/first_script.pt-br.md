---
title: "Programe o seu primeiro script Selenium"
linkTitle: "Primeiro Script"
weight: 8
needsTranslation: false
description: >
    Instruções passo a passo para programar um script Selenium
---

Assim que você tiver o [Selenium instalado]({{< ref "install_library.md" >}}), 
você estará pronto para programar códigos Selenium.

**Note**: if you get an error about drivers not found, please read about troubleshooting the
[driver location error]({{< ref "../troubleshooting/errors/driver_location.md" >}})

## Oito Componentes Básicos
Tudo que o Selenium faz é enviar comandos ao navegador de internet para fazer algo ou solicitar informações dele.
A maior parte do que você irá fazer com o Selenium é uma combinação desses comandos básicos:

### 1. Iniciando uma sessão
Para ter mais detalhes sobre como iniciar uma sessão, leia nossa documentação em [driver sessions]({{< ref "../drivers/" >}})

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L17" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L6" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L15" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L7" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L10" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L16" >}}
{{< /tab >}}
{{< /tabpane >}}

### 2. Agindo no navegador de internet
Nesse exemplo estamos [navegando]({{< ref "/documentation/webdriver/interactions/navigation.md" >}}) para uma página web. 

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L18" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L8" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L17" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L9" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L16" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L18" >}}
{{< /tab >}}
{{< /tabpane >}}

### 3. Solicitando informação do navegador de internet
Existem diversos tipos de [informação sobre o navegador de internet]({{< ref "/documentation/webdriver/interactions" >}}) que você
pode solicitar, incluindo window handles, tamanho / posição do navegador, cookies, alertas e etc.

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L20" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L10" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L19" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L11" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L18" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L20" >}}
{{< /tab >}}
{{< /tabpane >}}

### 4. Estabelecendo uma Estratégia de Espera

Sincronizar o código ao estado atual do navegador é um dos maiores 
desafios 
quando se trabalha com o Selenium, fazer isso de maneira bem feita é um tópico avançado.

Essencialmente, você quer ter certeza absoluta de que o elemento está na página antes de tentar localizá-lo
e o elemento está em um estado interativo antes de você tentar interagir com ele.

Uma espera implícita raramente é a melhor solução, mas é a mais fácil de demonstrar aqui, então
vamos usá-la como um substituto. 

Leia mais sobre [Estratégias de espera]({{< ref "/documentation/webdriver/waits.md" >}}).

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L23" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L13" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L22" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L14" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L21" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L23" >}}
{{< /tab >}}
{{< /tabpane >}}

### 5. Encontrando um elemento
A maioria dos comandos na maior parte das sessões do Selenium são relacionados a elementos e você não pode 
interagir
com um sem o primeiro [encontrando um elemento]({{< ref "/documentation/webdriver/elements" >}})

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L25-L26" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L15-L16" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L24-L25" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L16-L17" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L23-L24" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L25-L26" >}}
{{< /tab >}}
{{< /tabpane >}}

### 6. Agindo no elemento
Há apenas um punhado de [ações a serem executadas em um elemento]({{< ref "/documentation/webdriver/elements/interactions.md" >}}),
mas você irá usá-las com frequência.

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L28-L29" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L18-L19" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L27-L28" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L19-L20" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L26-L27" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L28-L29" >}}
{{< /tab >}}
{{< /tabpane >}}

### 7. Solicitando informações do elemento
Elementos podem guardar muitas [informações que podem ser solicitadas]({{< ref "/documentation/webdriver/elements/information" >}}).

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L32" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L22" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L31" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L23" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L30" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L32" >}}
{{< /tab >}}
{{< /tabpane >}}

### 8. Encerrando a sessão

Isso encerra o processo do driver, que por padrão também fecha o navegador.
Nenhum outro comando pode ser enviado para esta instância do driver.

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L35" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L25" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L34" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L26" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L13" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L35" >}}
{{< /tab >}}
{{< /tabpane >}}

## Juntando tudo
Vamos combinar essas 8 coisas em um script completo com asserções que podem ser executadas por um executor de testes.

{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
{{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java" >}}
{{< /tab >}}
{{< tab header="Python" >}}
{{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py" >}}
{{< /tab >}}
{{< tab header="CSharp" >}}
{{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs" >}}
{{< /tab >}}
{{< tab header="Ruby" >}}
{{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb" >}}
{{< /tab >}}
{{< tab header="JavaScript" >}}
{{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js" >}}
{{< /tab >}}
{{< tab header="Kotlin" >}}
{{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt" >}}
{{< /tab >}}
{{< /tabpane >}}

## Executando Testes
Se você esta usando selenium para realizar testes,
você deverá executar seu código usando feramentas para executar testes.

Muitos exemplos de código encontrado nessa documentação podem ser encontrado no nosso repositório de exemplos. 
Existem múltiplas opções em cada linguagem, mas esta será qual usaremos em nossos exemplos:


{{< tabpane text=true langEqualsHeader=true >}}
{{< tab header="Java" >}}
// Add instructions
{{< /tab >}}
{{< tab header="Python" >}}
// Add instructions
{{< /tab >}}
{{< tab header="CSharp" >}}
// Add instructions
{{< /tab >}}
{{< tab header="Ruby" >}}
// Add instructions
{{< /tab >}}
{{% tab header="JavaScript" text=true %}}
Install Mocha Test runner using below command in your terminal

Install with npm globally:

```shell
npm install -g mocha
```
or as a development dependency for your project:

```shell
npm install --save-dev mocha
```

and run your tests using below command

```shell
mocha firstScript.spec.js
```

{{< /tab >}}
{{< tab header="Kotlin" >}}
// Add instructions
{{< /tab >}}
{{< /tabpane >}}

## Próximos Passos

Use o que você aprendeu e construa o seu proprio código Selenium.

À medida que você encontrar mais funcionalidades de que necessita, leia o restante da nossa [documentação do WebDriver]({{< ref "/documentation/webdriver/" >}}).
