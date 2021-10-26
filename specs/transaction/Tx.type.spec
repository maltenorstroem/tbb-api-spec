name: Tx
type: Tx
description: Transaction type
lifecycle: null
__proto:
    package: transaction
    targetfile: transaction.proto
    imports: []
    options:
        go_package: github.com/maltenorstroem/tbb-api-spec/transaction;transactionpb
        java_multiple_files: "true"
        java_outer_classname: TransactionProto
        java_package: com.github.maltenorstroem.tbb.api.transaction
fields:
    from:
        type: string
        description: transfer from
        __proto:
            number: 1
        __ui: null
        meta:
            default: ""
            placeholder: transaction.tx.from.placeholder
            hint: ""
            label: transaction.tx.from.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    to:
        type: string
        description: transfer to
        __proto:
            number: 2
        __ui: null
        meta:
            default: ""
            placeholder: transaction.tx.to.placeholder
            hint: ""
            label: transaction.tx.to.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    value:
        type: uint32
        description: amount of transfer
        __proto:
            number: 3
        __ui: null
        meta:
            default: ""
            placeholder: transaction.tx.value.placeholder
            hint: ""
            label: transaction.tx.value.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    data:
        type: string
        description: additional data e.g. reward
        __proto:
            number: 4
        __ui: null
        meta:
            default: ""
            placeholder: transaction.tx.data.placeholder
            hint: ""
            label: transaction.tx.data.label
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
