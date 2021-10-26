name: BalanceCollection
type: BalanceCollection
description: Collectioncontainer which holds records of type transaction.Tx
lifecycle: null
__proto:
    package: balance
    targetfile: balance.proto
    imports:
        - furo/furo.proto
        - transaction/transaction.proto
    options:
        go_package: github.com/maltenorstroem/tbb-api-spec/balance;balancepb
        java_multiple_files: "true"
        java_outer_classname: BalanceProto
        java_package: com.github.maltenorstroem.tbb.api.balance
fields:
    meta:
        type: furo.Meta
        description: Meta for the response
        __proto:
            number: 3
        __ui: null
        meta:
            default: ""
            placeholder: balance.balancecollection.meta.placeholder
            hint: ""
            label: balance.balancecollection.meta.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    links:
        type: furo.Link
        description: the Hateoas links
        __proto:
            number: 2
        __ui: null
        meta:
            default: ""
            placeholder: balance.balancecollection.links.placeholder
            hint: ""
            label: balance.balancecollection.links.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: true
            typespecific: null
        constraints: {}
    entities:
        type: transaction.TxEntity
        description: the data contains a transaction.Tx
        __proto:
            number: 1
        __ui: null
        meta:
            default: ""
            placeholder: balance.balancecollection.entities.placeholder
            hint: ""
            label: balance.balancecollection.entities.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: true
            typespecific: null
        constraints: {}
