'''
def get_variant_data(product):
    variants_qs = VariantOption.objects.filter(
        product=product,
        status=StatusChoices.Active,
        stock__gt=0
    ).select_related("size", "color").order_by("id")

    variant = None
    for v in variants_qs:
        variant = v
        break

    sizes = []
    seen_sizes = set()

    for v in variants_qs:
        if v.size and v.size_id not in seen_sizes:
            sizes.append({
                "id": v.size_id,
                "code": v.size.title
            })
            seen_sizes.add(v.size_id)

    colors = []
    if variant and variant.size:
        seen_colors = set()
        for v in variants_qs:
            if v.color and v.color_id not in seen_colors:
                colors.append({
                    "id": v.color_id,
                    "code": v.color.title
                })
                seen_colors.add(v.color_id)
'''               
class User:
    def __init__(self, name, age=None):
        # age is optional parameter
        self.name = name
        self.age = age

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                