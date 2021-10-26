name: TxEntity
type: TxEntity
description: Entitycontainer which holds a transaction.Tx
lifecycle: null
__proto:
    package: transaction
    targetfile: transaction.proto
    imports:
        - furo/furo.proto
    options:
        go_package: github.com/maltenorstroem/tbb-api-spec/transaction;transactionpb
        java_multiple_files: "true"
        java_outer_classname: TransactionProto
        java_package: com.github.maltenorstroem.tbb.api.transaction
fields:
    data:
        type: transaction.Tx
        description: the data contains a transaction.Tx
        __proto:
            number: 1
        __ui: null
        meta:
            default: ""
            placeholder: transaction.txentity.data.placeholder
            hint: ""
            label: transaction.txentity.data.label
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
            placeholder: transaction.txentity.links.placeholder
            hint: ""
            label: transaction.txentity.links.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: true
            typespecific: null
        constraints: {}
    meta:
        type: furo.Meta
        description: Meta for the response
        __proto:
            number: 3
        __ui: null
        meta:
            default: ""
            placeholder: transaction.txentity.meta.placeholder
            hint: ""
            label: transaction.txentity.meta.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
