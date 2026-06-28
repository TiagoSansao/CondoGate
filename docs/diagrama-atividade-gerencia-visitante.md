```mermaid
flowchart TB

    start([Início])

    %% =======================
    %% PAPÉIS (swimlanes simples via subgraph)
    %% =======================

    subgraph Usuario[Visitante / Usuário]
        escolherAcao{Selecionar ação}
        selecionarVisitante[Selecionar visitante (CPF)]
        pegarNovosDados[Informar novos dados]
    end

    subgraph Sistema[Sistema]
        abrirMenu[Exibir menu de visitante]

        incluir[Incluir visitante]
        listar[Listar visitantes]
        alterar[Alterar visitante]
        remover[Remover visitante]

        inicioValidar[Validar entrada de dados]

        verificarCpfExistente{CPF já existe?}
        verificarCpfAlteracao{Novo CPF já existe?}

        buscarMorador[Buscar morador responsável]
        moradorExiste{Morador existe?}

        criarVisitante[Criar e salvar visitante]
        atualizarVisitante[Atualizar visitante]
        excluirVisitante[Remover visitante]

        listarDados[Obter lista de visitantes]
        listaVazia{Lista vazia?}

        mostrarLista[Exibir lista]
        mostrarSucesso[Exibir sucesso]
        mostrarErro[Exibir erro]
    end

    subgraph DAO[Banco de Dados / DAO]
        daoBuscarMorador[(Consultar morador)]
        daoSalvar[(Persistir visitante)]
        daoAtualizar[(Atualizar registro)]
        daoExcluir[(Excluir registro)]
        daoListar[(Listar registros)]
    end

    fim([Fim])

    %% =======================
    %% FLUXO PRINCIPAL
    %% =======================

    start --> abrirMenu --> escolherAcao

    escolherAcao -->|Incluir| incluir
    escolherAcao -->|Listar| listar
    escolherAcao -->|Alterar| alterar
    escolherAcao -->|Remover| remover
    escolherAcao -->|Retornar| fim

    %% =======================
    %% INCLUIR
    %% =======================

    incluir --> inicioValidar --> verificarCpfExistente

    verificarCpfExistente -->|[Sim]| mostrarErro
    verificarCpfExistente -->|[Não]| buscarMorador

    buscarMorador --> daoBuscarMorador --> moradorExiste

    moradorExiste -->|[Não]| mostrarErro
    moradorExiste -->|[Sim]| criarVisitante --> daoSalvar --> mostrarSucesso --> abrirMenu

    %% =======================
    %% LISTAR
    %% =======================

    listar --> listarDados --> daoListar --> listaVazia

    listaVazia -->|[Sim]| mostrarErro
    listaVazia -->|[Não]| mostrarLista --> abrirMenu

    %% =======================
    %% ALTERAR
    %% =======================

    alterar --> listarDados --> selecionarVisitante --> pegarNovosDados --> inicioValidar --> verificarCpfAlteracao

    verificarCpfAlteracao -->|[Sim]| mostrarErro
    verificarCpfAlteracao -->|[Não]| buscarMorador

    buscarMorador --> daoBuscarMorador --> moradorExiste

    moradorExiste -->|[Não]| mostrarErro
    moradorExiste -->|[Sim]| atualizarVisitante --> daoAtualizar --> mostrarSucesso --> abrirMenu

    %% =======================
    %% REMOVER
    %% =======================

    remover --> listarDados --> selecionarVisitante --> excluirVisitante --> daoExcluir --> mostrarSucesso --> abrirMenu

    %% =======================
    %% ERRO VOLTA MENU
    %% =======================

    mostrarErro --> abrirMenu
```
